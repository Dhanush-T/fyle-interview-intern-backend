from flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.assignments import Assignment

from .schema import AssignmentSchema, AssignmentGradeSchema, GetAssignmentGradeSchema
teachers_assignment_resources = Blueprint('teachers_assignment_resources', __name__)

@teachers_assignment_resources.route('/assignments', methods=['GET'], strict_slashes=False)
@decorators.auth_principal
def list_submitted_assignments(p):
    submitted_assignments = Assignment.get_assignments_by_teacher(p.teacher_id)
    submitted_assignments_dump = AssignmentSchema().dump(submitted_assignments, many=True)
    return APIResponse.respond(data=submitted_assignments_dump)

@teachers_assignment_resources.route('/assignments/grade', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def grade_submitted_assignment(p, incoming_payload):
    graded_assignment = AssignmentGradeSchema().load(incoming_payload)

    updated_graded_assignment = Assignment.update_grade(
        _id=graded_assignment.id,
        grade=graded_assignment.grade,
        principal=p
    )
    db.session.commit()
    updated_graded_assignment_dump = AssignmentSchema().dump(updated_graded_assignment)
    return APIResponse.respond(data=updated_graded_assignment_dump)



@teachers_assignment_resources.route('/assignments/grade/list', methods=['POST'], strict_slashes=False)
@decorators.accept_payload
@decorators.auth_principal
def list_by_grade_teacher(p, incoming_payload):
    list_assignment_by_grade = GetAssignmentGradeSchema().load(incoming_payload)

    teacher_list_assignments_by_grade = Assignment.get_assignments_by_grade_for_teachers(p.teacher_id, list_assignment_by_grade.grade)
    teacher_list_assignments_by_grade_dump = AssignmentSchema().dump(teacher_list_assignments_by_grade, many=True)
    return APIResponse.respond(data=teacher_list_assignments_by_grade_dump)

