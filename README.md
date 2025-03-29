# Welcome to Cardify
## Cardify API Documentation

Cardify is a RESTful API that provides digital identification solutions for NIN ID cards, Business IDs, and Driver’s Licenses. This API allows users to create, retrieve, and manage identity records.

## **Base URL**
All endpoints are prefixed with:
```
https://cardify-api-by76.onrender.com/
```

---

## **Endpoints Overview**

### **1. NIN ID Card Endpoint**
- **URL:** `/nin-info/`
- **Methods:** `GET`, `POST`
- **Description:**  
  - `GET`: Retrieve all stored NIN ID card records.  
  - `POST`: Submit new NIN ID card details.

#### **Expected Data for POST**
```json
{
  "full_name": "John Doe",
  "profile_pic": "image_url",
  "gender": "M",
  "address": "123 Main St",
  "nin": "12345678901",
  "dateofbirth": "2000-01-01",
  "country": "Nigeria",
  "state_of_origin": "Lagos"
}
```

#### **Frontend Integration Example (AJAX)**
```javascript
fetch("https://cardify-api.onrender.com/nin-info/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        full_name: "John Doe",
        profile_pic: "image_url",
        gender: "M",
        address: "123 Main St",
        nin: "12345678901",
        dateofbirth: "2000-01-01",
        country: "Nigeria",
        state_of_origin: "Lagos"
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

---

### **2. Business ID Endpoint**
- **URL:** `/business-info/`
- **Methods:** `GET`, `POST`
- **Description:**  
  - `GET`: Retrieve all business ID records.  
  - `POST`: Submit new business ID details.

#### **Expected Data for POST**
```json
{
  "full_name": "Acme Corporation",
  "job_title": "CEO",
  "profile_pic": "image_url",
  "gender": "F",
  "company_name": "Acme Inc",
  "company_logo": "logo_url",
  "phone_number": "08012345678",
  "email_address": "info@acme.com",
  "website": "https://www.acme.com"
}
```

#### **Frontend Integration Example (AJAX)**
```javascript
fetch("https://cardify-api.onrender.com/business-info/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
        full_name: "Acme Corporation",
        job_title: "CEO",
        profile_pic: "image_url",
        gender: "F",
        company_name: "Acme Inc",
        company_logo: "logo_url",
        phone_number: "08012345678",
        email_address: "info@acme.com",
        website: "https://www.acme.com"
    })
})
.then(response => response.json())
.then(data => console.log(data))
.catch(error => console.error("Error:", error));
```

---

## **Testing the API**
To interactively test the API, visit:  
```
https://cardify-api.onrender.com/test-form/
```
This test page allows you to input data and send requests to the API.

---

## **How to Embed Data in Templates**
### **Django Template Example**
If you are using Django templates to display API data dynamically, you can fetch data and pass it into the template using a context.

#### **Example (views.py)**
```python
import requests
from django.shortcuts import render

def nin_view(request):
    response = requests.get("https://cardify-api.onrender.com/nin-info/")
    data = response.json()
    return render(request, "nin_template.html", {"nin_records": data})
```

#### **Example (nin_template.html)**
```html
{% for record in nin_records %}
    <h2>{{ record.full_name }}</h2>
    <img src="{{ record.profile_pic }}" alt="Profile Picture">
    <p>NIN: {{ record.nin }}</p>
    <p>Address: {{ record.address }}</p>
{% endfor %}
```

---

## **Error Handling**
| Status Code | Meaning |
|-------------|---------|
| `200 OK` | Request was successful. |
| `201 Created` | New resource was successfully created. |
| `400 Bad Request` | Missing or invalid parameters. |
| `404 Not Found` | The requested resource does not exist. |
| `500 Internal Server Error` | Server encountered an unexpected issue. |

---

## **Project Setup**
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/cardify.git
   cd cardify
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the Django server:
   ```sh
   python manage.py runserver
   ```

---

## **Contributors**
- **Backend Developer:** Gaji Yaqub Ayomikun ([@codewithgaji](https://x.com/codewithgaji))
- **Frontend Developer:** Perpetual Uche ([@uche.dev](https://x.com/perpetualuchec5))

---

## **License**
This project is open-source and licensed under the MIT License.

---

## **Final Notes**
- This README provides **detailed documentation** on **API usage** and **how to integrate it** into Django templates.
