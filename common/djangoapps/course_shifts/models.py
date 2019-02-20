"""
This file contains the logic for course shifts.
"""
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

    class Meta:
        db_table = 'course_shifts'

    def to_dict(self, add_number_of_students=False):
        data = {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.strftime(SHIFT_DATE_FORMAT),
            'enrollment_start_date': self.enrollment_start_date.strftime(SHIFT_DATE_FORMAT),
            'enrollment_end_date': self.enrollment_end_date.strftime(SHIFT_DATE_FORMAT),
            'studio_version': self.studio_version
        }
        if add_number_of_students and self.id:
            number_of_students = CourseShiftUser.objects.filter(course_key=self.course_key, course_shift=self).count()
            data['number_of_students'] = number_of_students
        return data


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
