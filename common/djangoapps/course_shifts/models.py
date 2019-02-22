"""
This file contains the logic for course shifts.
"""
import datetime
from django.contrib.auth.models import User
from django.db import models
from opaque_keys.edx.django.models import CourseKeyField


SHIFT_DATE_FORMAT = '%Y-%m-%d %H:%M'


class CourseShift(models.Model):
    course_key = CourseKeyField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField(verbose_name='Start Date', null=False, blank=False)
    enrollment_start_date = models.DateTimeField(verbose_name='Enrollment Start Date', null=False, blank=False)
    enrollment_end_date = models.DateTimeField(verbose_name='EnrollmentStart Date', null=False, blank=False)
    studio_version = models.BooleanField(verbose_name='Course shift related to studio settings', default=False)
    enabled = models.BooleanField(verbose_name='Course shifts are enabled for course', default=False)

    class Meta:
        db_table = 'course_shifts'

    def to_dict(self, add_number_of_students=False, convert_dates_to_str=True):
        data = {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.strftime(SHIFT_DATE_FORMAT) if convert_dates_to_str else self.start_date,
            'enrollment_start_date': self.enrollment_start_date.strftime(SHIFT_DATE_FORMAT) if convert_dates_to_str else self.enrollment_start_date,
            'enrollment_end_date': self.enrollment_end_date.strftime(SHIFT_DATE_FORMAT) if convert_dates_to_str else self.enrollment_end_date,
            'studio_version': self.studio_version
        }
        if add_number_of_students and self.id:
            number_of_students = CourseShiftUser.objects.filter(course_key=self.course_key, course_shift=self).count()
            data['number_of_students'] = number_of_students
        return data

    @classmethod
    def get_course_shift(cls, course_key, user=None):
        if isinstance(course_key, list):
            return cls.get_courses_shifts_by_current_date(course_key, user)
        else:
            course_shift = cls.get_course_shift_by_current_date(course_key, user)
            return course_shift.to_dict(convert_dates_to_str=False) if course_shift else None

    @classmethod
    def get_course_shift_by_current_date(cls, course_key, user=None):
        dt_now = datetime.datetime.utcnow()

        if user is not None and user.is_authenticated:
            try:
                course_shift_user = CourseShiftUser.objects.get(course_key=course_key, user=user)
                if course_shift_user.course_shift.enabled:
                    return course_shift_user.course_shift
            except CourseShiftUser.DoesNotExist:
                pass

        course_shift = CourseShift.objects.filter(
            course_key=course_key,
            enabled=True,
            enrollment_start_date__lte=dt_now,
            enrollment_end_date__gte=dt_now).order_by('start_date').first()

        return course_shift

    @classmethod
    def get_courses_shifts_by_current_date(cls, courses_keys, user=None):
        dt_now = datetime.datetime.utcnow()

        result = {}
        users_shifts = {}

        if user is not None and user.is_authenticated:
            course_shift_user = CourseShiftUser.objects.filter(course_key__in=courses_keys, user=user)
            for cu in course_shift_user:
                k = str(cu.course_key)
                result[k] = cu.course_shift.to_dict(convert_dates_to_str=False)
                users_shifts[k] = True

        course_shifts = CourseShift.objects.filter(
            course_key__in=courses_keys,
            enabled=True,
            enrollment_start_date__lte=dt_now,
            enrollment_end_date__gte=dt_now).order_by('start_date')

        for c in course_shifts:
            k = str(c.course_key)
            if not users_shifts.get(k, False) and (k not in result or c.start_date < result[k]['start_date']):
                result[k] = c.to_dict(convert_dates_to_str=False)
        return result


class CourseShiftUser(models.Model):
    course_key = CourseKeyField(max_length=255, db_index=True)
    course_shift = models.ForeignKey(CourseShift)
    user = models.ForeignKey(User)

    class Meta:
        db_table = 'course_shift_user'
        unique_together = (('user', 'course_key'),)


def allow_to_change_deadline(course_key, user):
    try:
        course_shift_user = CourseShiftUser.objects.get(course_key=course_key, user=user)
        course_shift = CourseShift.objects.filter(course_key=course_key,
                                                  start_date__gt=course_shift_user.course_shift.start_date)\
            .order_by('-start_date').first()
        if course_shift:
            return True, course_shift
    except CourseShiftUser.DoesNotExist:
        pass
    return False, None
