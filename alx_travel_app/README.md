# ALX Travel App - Task 0x00

## Database Modeling and Data Seeding in Django

This project implements the database models, serializers, and seeding functionality for an AirBnB-like application as part of the ALX Travel App coursework.

## Project Structure

```
alx_travel_app/
├── listings/
│   ├── models.py              # Database models (Listing, Booking, Review)
│   ├── serializers.py         # API serializers (Listing, Booking)
│   ├── management/
│   │   └── commands/
│   │       └── seed.py        # Database seeding command
│   └── ...
├── README.md                  # This file
└── ...
```

## Models Implemented

### 1. Listing Model
- **listing_id**: Primary Key (UUID)
- **host_id**: Foreign Key to User
- **name**: Property name
- **description**: Property description
- **location**: Property location
- **price_per_night**: Decimal price
- **created_at/updated_at**: Timestamps

### 2. Booking Model
- **booking_id**: Primary Key (UUID)
- **property_id**: Foreign Key to Listing
- **user_id**: Foreign Key to User
- **start_date/end_date**: Booking dates
- **total_price**: Booking total cost
- **status**: Enum (pending, confirmed, canceled)
- **created_at**: Timestamp

### 3. Review Model
- **review_id**: Primary Key (UUID)
- **property_id**: Foreign Key to Listing
- **user_id**: Foreign Key to User
- **rating**: Integer (1-5)
- **comment**: Review text
- **created_at**: Timestamp

## Serializers

### ListingSerializer
- Handles all Listing model fields
- Validates price_per_night is positive
- Read-only fields: listing_id, created_at, updated_at

### BookingSerializer
- Handles all Booking model fields
- Validates end_date is after start_date
- Validates total_price is positive
- Read-only fields: booking_id, created_at

## Database Seeding

The seeding command populates the database with sample data for testing and development.

### Running the Seed Command

```bash
# Basic seeding with default values
python manage.py seed

# Custom quantities
python manage.py seed --users 50 --listings 30 --bookings 100 --reviews 80

# Clear existing data before seeding
python manage.py seed --clear

# Help
python manage.py seed --help
```

### Seed Command Options

- `--users`: Number of users to create (default: 20)
- `--listings`: Number of listings to create (default: 15)
- `--bookings`: Number of bookings to create (default: 30)
- `--reviews`: Number of reviews to create (default: 25)
- `--clear`: Clear existing data before seeding

### Sample Data Generated

- **Users**: Random users with realistic names, emails, and usernames
- **Listings**: Properties in various US cities with realistic descriptions and pricing
- **Bookings**: Reservations with random dates and calculated pricing
- **Reviews**: Property reviews with ratings and comments

## Installation and Setup

1. Ensure you have the Django project set up
2. Install required dependencies:
   ```bash
   pip install faker
   ```
3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Seed the database:
   ```bash
   python manage.py seed
   ```

## Key Features

- **UUID Primary Keys**: All models use UUID for primary keys for better scalability
- **Data Validation**: Comprehensive validation in both models and serializers
- **Realistic Sample Data**: Uses Faker library to generate realistic test data
- **Indexed Fields**: Important fields are indexed for better query performance
- **Relationships**: Proper foreign key relationships between models
- **Constraints**: Database-level constraints for data integrity

## Usage

After seeding, you can:
- View the created data in Django admin
- Use the serializers in your API views
- Query the models in your application logic
- Test your application with realistic sample data

## Database Schema

The models follow the provided AirBnB database specification with appropriate:
- Primary and foreign key relationships
- Data types and constraints
- Indexing for performance
- Model methods and string representations

---

**Repository**: `alx_travel_app_0x01`  
**Directory**: `alx_travel_app`  
**Author**: ALX Student


## API Endpoints (Task 0x01: CRUD Implementation)

The following RESTful API endpoints have been implemented using Django REST Framework ViewSets and Routers, and are automatically documented via Swagger at `/swagger/` and Redoc at `/redoc/`.

| Resource | Method | Endpoint | Description | Authentication |
| :--- | :--- | :--- | :--- | :--- |
| **Listings** | `GET` | `/api/listings/` | List all property listings. | None (AllowAny) |
| **Listings** | `POST` | `/api/listings/` | Create a new listing (Host). | Required (IsAuthenticated) |
| **Listing Detail**| `GET` | `/api/listings/{id}/` | Retrieve a specific listing. | None (AllowAny) |
| **Listing Detail**| `PUT`/`PATCH`/`DELETE`| `/api/listings/{id}/` | Update or Delete a listing. | Required (IsAuthenticated) |
| **Bookings** | `GET` | `/api/bookings/` | List all bookings. | Required (IsAuthenticated) |
| **Bookings** | `POST` | `/api/bookings/` | Create a new booking (Guest). | Required (IsAuthenticated) |
| **Booking Detail**| `GET`/`PUT`/`PATCH`/`DELETE`| `/api/bookings/{id}/` | Manage a specific booking. | Required (IsAuthenticated) |