from student.roles import CourseStaffRole, CourseInstructorRole, CourseCreatorRole
from student.models import CourseAccessRole

# Role name for OrgStaffRole, OrgInstructorRole has hardcoded in __init__ method ("staff" and "instructor")
LIBRARY_CREATE_ROLES = [
    'staff',
    'instructor',
    CourseInstructorRole.ROLE,
    CourseStaffRole.ROLE,
    CourseCreatorRole.ROLE
]


def can_create_library(user):
    qs = CourseAccessRole.objects.filter(user_id=user.id, role__in=LIBRARY_CREATE_ROLES)
    is_library_creator = qs.exists()
    return is_library_creator
