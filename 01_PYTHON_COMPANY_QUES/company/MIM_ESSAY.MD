Sure! Here are the answers to your questions:

### 1. Five Self-Closing Tags
- `<br />`
- `<img />`
- `<input />`
- `<hr />`
- `<meta />`

### 2. Program to Remove Duplicates from Array Without Using In-Build Function
```javascript
let list = [2, 3, 4, 4, 5, 6, 6, 6, 7, 7, 8, 8, 8, 13, 2, 4, 4, 10];
let uniqueList = [];

for (let i = 0; i < list.length; i++) {
    if (uniqueList.indexOf(list[i]) === -1) {
        uniqueList.push(list[i]);
    }
}

console.log(uniqueList);
```

### 3. How to Import CSS in an HTML Page
You can import CSS in an HTML page using the `<link>` tag in the `<head>` section:
```html
<head>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
```

### 4. SQL Query to Get User Details from User Table Where User Name Starts with "R"
```sql
SELECT * FROM user WHERE user_name LIKE 'R%';
```

### 5. Jobs and Queue
In programming, a job queue is a data structure that holds tasks (jobs) waiting to be executed. Jobs are processed in a specific order, often using a first-in, first-out (FIFO) method. This is commonly used in background processing or task scheduling.

### 6. HTTP Methods
Common HTTP methods include:
- **GET**: Retrieve data from a server.
- **POST**: Send data to a server to create/update a resource.
- **PUT**: Update a resource.
- **DELETE**: Remove a resource.
- **PATCH**: Apply partial modifications to a resource.

### 7. Program to Get the Length of a String Without Using In-Build Function or Property
```javascript
function getStringLength(str) {
    let length = 0;
    for (let char of str) {
        length++;
    }
    return length;
}

let str = "Danish Khan";
console.log(getStringLength(str));
```

### 8. AJAX
AJAX (Asynchronous JavaScript and XML) is a technique used to send and receive data asynchronously without refreshing the web page. It allows web applications to update parts of a page with new data.

### 9. What is CORS?
CORS (Cross-Origin Resource Sharing) is a security feature implemented by web browsers that allows or restricts web applications from making requests to a domain different from the one that served the web page. It helps prevent malicious sites from accessing sensitive data on another domain. CORS is managed through HTTP headers that specify which origins are permitted to access resources.