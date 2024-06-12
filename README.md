# Website Visits Tracking API

This Flask application provides endpoints to track and retrieve website visit statistics. The API allows tracking visits by customers using different devices and retrieving visit counts for individual customers and the overall site.

## Endpoints

### 1. Track a Visit to a Website

**Endpoint:** `/visit_website`  
**Method:** `POST`  
**Description:** Track a visit to a website by a specific customer using a specific device. Each customer visit is counted only once, regardless of the device used.

**Request Body:**
```json
{
  "customerId": "string",
  "deviceId": "string",
  "websiteId": "string"
}
```

**Response:**
```json
{
  "message": "Visit tracked successfully."
}
```

### 2. Get the Number of Visits for a Specific Customer

**Endpoint:** `/get_website_visit_count_for_customer`  
**Method:** `GET`  
**Description:** Retrieve the number of visits a specific customer has made to a specific website.

**Query Parameters:**
- `customerId` (required): The ID of the customer.
- `websiteId` (required): The ID of the website.

**Response:**
```json
{
  "customerId": "string",
  "websiteId": "string",
  "visitCount": integer
}
```

### 3. Get the Total Number of Visits to a Website

**Endpoint:** `/get_overall_website_hit_count`  
**Method:** `GET`  
**Description:** Retrieve the total number of visits to a specific website by all customers.

**Query Parameters:**
- `websiteId` (required): The ID of the website.

**Response:**
```json
{
  "websiteId": "string",
  "overallHitCount": integer
}
```

## Running the Application

To run the Flask application, follow these steps:

1. Ensure you have Python installed (version 3.6 or higher).
2. Install Flask:
   ```bash
   pip install flask
   ```
3. Save the provided code in a file named `app.py`.
4. Run the Flask application:
   ```bash
   python app.py
   ```

The application will start on `http://127.0.0.1:5000/` by default.

## Example JSON Input for Testing

Here is an example JSON input to test the `/visit_website` endpoint using Postman or a similar tool:

```json
{
  "customerId": "customer1",
  "deviceId": "device1",
  "websiteId": "website1"
}
```

## Notes

- The application uses an in-memory data structure (`website_visits`) to store visit data. This means all data will be lost when the application stops.
- Ensure that the JSON keys in the request body match the keys used in the code (e.g., `customerId`, `deviceId`, `websiteId`).
