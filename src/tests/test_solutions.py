from textwrap import dedent


def test_homeworks(client):
    response = client.get('/homeworks')
    assert response.json()


def test_solution_simple(client):
    response = client.post(
        url='/solutions/1/auto',
        json={
            "content": 'print("Hello world!")'
        })
    assert response.json()['success'], response.json()


def test_solution_input_floats(client):
    response = client.post(
        url='/solutions/2/auto',
        json={
            "content": dedent('''
            a, b, c = [float(x) for x in input().split()]
            result = a + b * ( c / 2 )
            print(result)
            ''')
        })
    assert response.json()['success'], response.json()


def test_solution_input_strings(client):
    response = client.post(
        url='/solutions/5/auto',
        json={
            "content": dedent('''
            s = input()
            result = ''.join(x.capitalize() for x in s.split('_'))
            print(result)
            ''')
        })
    assert response.json()['success'], response.json()


def test_solution_input_function(client):
    response = client.post(
        url='/solutions/15/auto',
        json={
            "content": dedent('''
            def solution(lst):
                return max(lst) - min(lst)
            ''')
        })
    assert response.json()['success'], response.json()
