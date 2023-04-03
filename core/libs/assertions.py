from .exceptions import FyleError
from marshmallow.exceptions import ValidationError


def base_assert(error_code, msg):
    raise FyleError(status_code=error_code, message=msg)


def assert_auth(cond, msg='UNAUTHORIZED'):
    if cond is False:
        base_assert(401, msg)


def assert_true(cond, msg='FORBIDDEN'):
    if cond is False:
        base_assert(403, msg)


def assert_valid(cond, msg='BAD_REQUEST'):
    if cond is False:
        base_assert(400, msg)
    
def assert_submitted(cond, msg='ALREADY_SUBMITTED'):
    if(cond == "SUBMITTED"):
        base_assert(400, msg)

def assert_found(_obj, msg='NOT_FOUND'):
    if _obj is None:
        base_assert(404, msg)

def assert_valid_grade(cond, msg='INVALID_GRADE'):
    if(cond is False):
        raise ValidationError(msg)

def assert_grade_drafted(cond, msg='DRAFTED_ASSIGNMENTS_NOT_GRADED'):
    if(cond == "DRAFT"):
        base_assert(400, msg)
    
def assert_cross_submit(cond, msg='CROSS_SUBMISSION'):
    if(cond is True):
        base_assert(400, msg)