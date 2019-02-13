import json

from django.views.decorators.http import require_POST
from dateutil.parser import parse
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.translation import ugettext as _

from .models import CourseShift, CourseShiftUser
from edxmako.shortcuts import render_to_response
from util.json_request import JsonResponse
from opaque_keys.edx.keys import CourseKey
from opaque_keys import InvalidKeyError
from xmodule.modulestore.django import modulestore
from xmodule.modulestore.exceptions import ItemNotFoundError


def check_course_exists(func):
    def wrapper(self, request, course_id):
        try:
            course_key = CourseKey.from_string(course_id)
            course = modulestore().get_course(course_key)
        except (InvalidKeyError, ItemNotFoundError):
            return JsonResponse({"success": False, "errorMessage": _("Course not found")}, status=404)
        return func(self, request, course)
    return wrapper


@login_required
@check_course_exists
def get_course_shifts(request, course):
    data = CourseShift.objects.filter(course_key=course.id).order_by('start_date', 'enrollment_start_date')
    return JsonResponse({"success": True, "data": [item.to_dict() for item in data]})


@login_required
@require_POST
@check_course_exists
def update_course_shifts(request, course):
    try:
        posted_data = json.loads(request.body.decode('utf-8'))
    except ValueError:
        return JsonResponse({"success": False, "errorMessage": _("Invalid request")})

    post_required_params = {
        'title': 'Course Shift',
        'startDate': 'Start Date',
        'enrollStartDate': 'Enrollment Start Date',
        'enrollEndDate': 'Enrollment End Date'
    }

    for k, v in post_required_params.iteritems():
        if k not in posted_data or posted_data[k].strip() == '':
            return JsonResponse({"success": False, "errorMessage": _(v + " field can't be empty")})

    name = posted_data['title'].strip()
    start_date = posted_data['startDate'].strip()
    enrollment_start_date = posted_data['enrollStartDate'].strip()
    enrollment_end_date = posted_data['enrollEndDate'].strip()

    if not name or not start_date or not enrollment_start_date or not enrollment_end_date:
        return JsonResponse({
            "success": False,
            "errorMessage": _("Some required fields were not passed")
        })

    try:
        course_shift_id = int(posted_data['id']) if 'id' in posted_data else None
    except ValueError:
        return JsonResponse({
            "success": False,
            "errorMessage": _("Invalid Course Shift ID format")
        })

    try:
        start_date = parse(start_date).date()
    except ValueError as e:
        return JsonResponse({
            "success": False,
            "errorMessage": _("Start date is invalid: ") + str(e)
        })

    try:
        enrollment_start_date = parse(enrollment_start_date).date()
    except ValueError as e:
        return JsonResponse({
            "success": False,
            "errorMessage": _("Enrollment start date is invalid: ") + str(e)
        })

    try:
        enrollment_end_date = parse(enrollment_end_date).date()
    except ValueError as e:
        return JsonResponse({
            "success": False,
            "errorMessage": _("Enrollment end date is invalid: ") + str(e)
        })

    if enrollment_start_date >= enrollment_end_date:
        return JsonResponse({
            "success": False,
            "errorMessage": _("Enrollment Date must be after the Start Date")
        })

    if enrollment_start_date >= start_date:
        return JsonResponse({
            "success": False,
            "errorMessage": _("The course start date must be later than the enrollment start date.")
        })

    overlap_items = CourseShift.objects.filter(
        Q(course_key=course.id,
          enrollment_start_date__lte=enrollment_start_date,
          enrollment_end_date__gte=enrollment_start_date) |
        Q(course_key=course.id,
          enrollment_start_date__lte=enrollment_end_date,
          enrollment_end_date__gte=enrollment_end_date))

    if overlap_items:
        for overlap_item in overlap_items:
            if (course_shift_id and course_shift_id != overlap_item.id) or course_shift_id is None:
                overlap_item_dict = overlap_item.to_dict()
                return JsonResponse({
                    "success": False,
                    "errorMessage": _("New course shift interval overlaps with the interval for"
                                      " \"%(name)s\" (%(enrollment_start_date)s - %(enrollment_end_date)s)" % overlap_item_dict)
                })

    if course_shift_id:
        try:
            obj = CourseShift.objects.get(pk=course_shift_id, course_key=course.id)
            obj.name = name
            obj.start_date = start_date
            obj.enrollment_start_date = enrollment_start_date
            obj.enrollment_end_date = enrollment_end_date
        except ObjectDoesNotExist:
            return JsonResponse({"success": False, "errorMessage": _("Term was not found")})
    else:
        obj = CourseShift(
            course_key=course.id,
            name=name,
            start_date=start_date,
            enrollment_start_date=enrollment_start_date,
            enrollment_end_date=enrollment_end_date
        )
    obj.save()
    return JsonResponse({"success": True, "course_shift": {"id": obj.id}})


@login_required
@check_course_exists
def find_user(request, course):
    user_token = request.GET.get('user_token')

    user = User.objects.filter(Q(username=user_token)|Q(email=user_token)).first()
    if user:
        return JsonResponse({
            "success": False,
            "user_id": None,
            "error": _("User not found")
        })

    try:
        obj = CourseShiftUser.objects.filter(user=user)
        return JsonResponse({
            "success": True,
            "user_id": user.id,
            "course_shift": obj.course_shift.to_dict()
        })
    except CourseShiftUser.DoesNotExist:
        return JsonResponse({
            "success": True,
            "user_id": user.id,
            "course_shift": None
        })


@login_required
@require_POST
@check_course_exists
def update_user(request, course):
    pass


@login_required
@require_POST
@check_course_exists
def update_deadlines(request, course):
    pass
