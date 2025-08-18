Here's a breakdown of the different types of relationships in Django, including **OneToOne**, **ManyToOne**, **OneToMany**, and **ManyToMany**, along with examples for each:

### 1. OneToOne Relationship

**Definition**: A one-to-one relationship means that each instance of one model is associated with exactly one instance of another model.

**Example**:
```python
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

**Usage**:
- Each `User` can have one `UserProfile`.
- Accessing the profile: `user.userprofile`.

### 2. ManyToOne Relationship

**Definition**: A many-to-one relationship means that many instances of one model can be associated with a single instance of another model.

**Example**:
```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

**Usage**:
- Many `Books` can be written by one `Author`.
- Accessing the author of a book: `book.author`.

### 3. OneToMany Relationship

**Definition**: A one-to-many relationship is essentially the inverse of a many-to-one relationship. It means one instance of a model can relate to multiple instances of another model.

**Example**:
- This is represented through a foreign key in the related model.
- Using the previous example, one `Author` can have many `Books`.

**Usage**:
- Accessing books by an author: `author.book_set.all()`.

### 4. ManyToMany Relationship

**Definition**: A many-to-many relationship means that multiple instances of one model can be associated with multiple instances of another model.

**Example**:
```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    title = models.CharField(max_length=200)
    students = models.ManyToManyField(Student)
```

**Usage**:
- A `Student` can enroll in multiple `Courses`, and a `Course` can have multiple `Students`.
- Accessing students in a course: `course.students.all()`.

### Summary Table

| Relationship Type | Definition | Example |
|-------------------|------------|---------|
| **OneToOne**      | One instance of a model is related to one instance of another model. | User and UserProfile |
| **ManyToOne**     | Many instances of one model relate to one instance of another model. | Books and Author |
| **OneToMany**     | One instance of a model relates to multiple instances of another model (achieved via ForeignKey). | Author and Books |
| **ManyToMany**    | Multiple instances of one model relate to multiple instances of another model. | Students and Courses |

These relationships help structure and normalize your database effectively in Django. Let me know if you need further clarification or additional examples!