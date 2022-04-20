try:
    from flaskapi import app
    import unittest

except Exception as e:
    print("Some Modules are Missing {} ".format(e))


# run these tests for each app route on flaskapi module
class FlaskTest(unittest.TestCase):
    # Check for response 200
    def test_checklist(self):
        # Check for response 200
        tester = app.test_client(self)
        response = tester.get("/checklist")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # Check if content is json
    def test_checklist_content(self):
        tester = app.test_client(self)
        response = tester.get("/checklist")
        self.assertEqual(response.content_type, "application/json")

    # Check message of data
    def test_checklist_data(self):
        tester = app.test_client(self)
        response = tester.get("/checklist")
        self.assertTrue(b'Message' in response.data)

    def test_checklist(self):
        # Check for response 200
        tester = app.test_client(self)
        response = tester.get("/upload")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)



if __name__ == "__main__":
    unittest.main()