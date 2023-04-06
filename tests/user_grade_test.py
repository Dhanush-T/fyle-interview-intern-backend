def test_graded_assignment1(client, h_teacher_1):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_1,
        json={
            "id":  1,
            "grade": "A"
        }
    )

    assert response.status_code == 200
    data = response.json['data']

    assert data['teacher_id'] == 1
    assert data['grade'] == 'A'


def test_graded_assignment2(client, h_teacher_2):
    response = client.post(
        '/teacher/assignments/grade',
        headers=h_teacher_2,
        json={
            "id":  3,
            "grade": "B"
        }
    )

    assert response.status_code == 200
    data = response.json['data']

    assert data['teacher_id'] == 2
    assert data['grade'] == 'B'


def test_studentsList_assignment_by_grade(client, h_student_1):
    grade = 'A'
    response = client.post(
        '/student/assignments/grade',
        headers=h_student_1,
        json={
            'grade': 'A'
        })

    assert response.status_code == 200
    data = response.json['data']

    for assignment in data:
        assert assignment['student_id'] == 1
        assert assignment['grade'] == grade

def test_teachers_list_by_grade(client, h_teacher_1):
    grade = 'A'
    response = client.post(
        '/teacher/assignments/grade/list',
        headers=h_teacher_1,
        json={
            'grade': 'A'
        })

    assert response.status_code == 200
    data = response.json['data']

    for assignment in data:
        assert assignment['teacher_id'] == 1
        assert assignment['grade'] == grade