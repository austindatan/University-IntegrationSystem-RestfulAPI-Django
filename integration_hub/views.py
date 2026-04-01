import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UniversityIntegrationView(APIView):
    def get(self, request, student_id):
        base_url = "http://127.0.0.1:8000/api"
        
        try:
            student_res = requests.get(f"{base_url}/students/students/{student_id}/")
            library_res = requests.get(f"{base_url}/library/records/")
            payment_res = requests.get(f"{base_url}/payments/records/")

            if student_res.status_code != 200:
                return Response({"error": "Student not found in Student App"}, status=status.HTTP_404_NOT_FOUND)

            student_data = student_res.json()
            library_all = library_res.json() if library_res.status_code == 200 else []
            payment_all = payment_res.json() if payment_res.status_code == 200 else []

            student_library = next((item for item in library_all if item['student_id'] == student_id), {"message": "No library record found"})
            student_payments = [item for item in payment_all if item['student_id'] == student_id]

            integrated_report = {
                "student_info": {
                    "id": student_data.get("student_id"),
                    "full_name": student_data.get("name"),
                    "course": student_data.get("course")
                },
                "library_status": student_library,
                "billing_summary": {
                    "total_payments_made": len(student_payments),
                    "history": student_payments
                }
            }

            return Response(integrated_report)

        except requests.exceptions.ConnectionError:
            return Response({"error": "One or more subsystems are offline"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)