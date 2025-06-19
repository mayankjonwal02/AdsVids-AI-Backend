# Amazon Product Video Ad Script Generator API Documentation

## Base URL
```
http://localhost:8000
```

## Endpoints

### 1. Health Check
Check if the API is running.

**GET /** 
```
GET /
```

**Response**
```json
{
    "message": "Welcome to the Product API! Use /products to manage products."
}
```

### 2. Generate Ad Script
Generate a video advertisement script from an Amazon product URL.

**POST /get_script**
```
POST /get_script
```

**Request Body**
```json
{
    "url": "string"  // Amazon product URL
}
```

**Response Body**
```json
{
    "script": "string",  // Generated video script
    "images": [         // Array of product images
        "string"        // Image URLs
    ]
}
```

**Error Response**
```json
{
    "error": "string"   // Error message if something goes wrong
}
```

## Example Usage

### Generate Ad Script Request
```bash
curl -X POST "http://localhost:8000/get_script" \
     -H "Content-Type: application/json" \
     -d '{
           "url": "https://www.amazon.com/product-example"
         }'
```

### Successful Response
```json
{
    "script": "[CHEERFUL MUSIC BEGINS]\nNARRATOR (VO): \"Looking for the perfect....\"\n[INTRO / PRODUCT SHOT]\n...",
    "images": [
        "https://m.media-amazon.com/images/I/71example1.jpg",
        "https://m.media-amazon.com/images/I/71example2.jpg"
    ]
}
```

### Error Response
```json
{
    "error": "Failed to scrape product data"
}
```

## Notes
- The API scrapes Amazon product pages to generate video ad scripts
- Scripts are generated using AI (Groq LLM)
- Response time may vary depending on the scraping and AI generation process
- All product images are returned in high resolution format
