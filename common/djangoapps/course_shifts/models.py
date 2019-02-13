"""
This file contains the logic for course shifts.
"""
from django.contrib.auth.models import User
from django.db import models
from opaque_keys.edx.django.models import CourseKeyField


class CourseShift(models.Model):
    course_key = CourseKeyField(max_length=255, db_index=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField(verbose_name='Start Date', null=False, blank=False)
    enrollment_start_date = models.DateField(verbose_name='Enrollment Start Date', null=False, blank=False)
    enrollment_end_date = models.DateField(verbose_name='EnrollmentStart Date', null=False, blank=False)

    class Meta:
        db_table = 'course_shifts'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'start_date': self.start_date.strftime('%-m/%-d/%Y'),
            'enrollment_start_date': self.enrollment_start_date.strftime('%-m/%-d/%Y'),
            'enrollment_end_date': self.enrollment_end_date.strftime('%-m/%-d/%Y')
        }


class CourseShiftUser(models.Model):
    course_key = CourseKeyField(max_length=255, db_index=True)
    course_shift = models.ForeignKey(CourseShift)
    user = models.ForeignKey(User)

    class Meta:
        db_table = 'course_shift_user'
        unique_together = (('user', 'course_key'),)
