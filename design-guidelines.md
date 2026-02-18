# Rider Management App -- Design & Development Guidelines

## 1. Project Overview

This application is built using Django and focuses on managing rider
performance data, including:

-   Rider personal information
-   Assigned bike details
-   Total rides completed
-   Commission earned
-   Performance metrics
-   Activity history

The system must be scalable, secure, and production-ready from day one.

Everything revolves around clarity, reusability, and real-world
practicality.

------------------------------------------------------------------------

## 2. Core Principles (Non-Negotiable)

### DRY (Don't Repeat Yourself)

DRY is not a guideline --- it is a limitation.

-   If logic appears more than once → extract it.
-   If code feels reusable → make it reusable.
-   If a pattern repeats → centralize it.
-   Shared logic must live in utilities, services, helpers, or base
    classes.

No exceptions.

Every repeated line is technical debt.

------------------------------------------------------------------------

## 3. UI & Styling Rules

### Framework

All UI must be built using Bootstrap.

### Strict Styling Policy

-   NO custom CSS unless Bootstrap cannot achieve the design.
-   NO inline styles.
-   NO component-specific CSS files unless absolutely required.

Bootstrap utilities must always be preferred.

------------------------------------------------------------------------

### Colors (Only Allowed Custom Styling)

Custom colors are allowed but must follow this structure:

:root { --primary: #xxxxxx; --secondary: #xxxxxx; --success: #xxxxxx;
--danger: #xxxxxx; }

Rules:

-   Colors must be declared ONCE.
-   Reused everywhere via variables.
-   No hardcoded colors in templates.
-   No random hex values.

------------------------------------------------------------------------

## 4. Frontend JavaScript Rules

### DRY Enforcement

-   Shared behaviors → shared functions.
-   Repeated DOM logic → helper methods.
-   Reused API calls → centralized fetch layer.

If something is used twice, it becomes a function.

------------------------------------------------------------------------

### JavaScript Standards

-   Use modern ES6+
-   Prefer const and let
-   Avoid global variables
-   Modularize scripts
-   Never duplicate logic
-   Defensive coding only

------------------------------------------------------------------------

### Security

-   Sanitize all inputs
-   Escape outputs
-   Prevent XSS
-   Never expose secrets
-   No inline scripts
-   Use CSRF tokens always

Memory leaks and dangling listeners are unacceptable.

------------------------------------------------------------------------

## 5. Backend (Django) Architecture Rules

### DRY Is Mandatory

DRY is enforced at:

-   Views
-   Services
-   Models
-   Serializers
-   Validators
-   Utilities

Rules:

-   Shared business logic goes into service layers.
-   Views only orchestrate.
-   Models represent data only.
-   Validation is centralized.
-   Queries are reusable.

Never repeat ORM logic.

------------------------------------------------------------------------

### Folder Structure (Recommended)

app/ ├── models/ ├── services/ ├── views/ ├── serializers/ ├──
validators/ ├── utils/

Each layer has one responsibility.

------------------------------------------------------------------------

## 6. Business Logic Rules

### Services Layer

All calculations must live in services:

-   Commission computation
-   Ride aggregation
-   Performance scoring
-   Earnings summaries

Views must NEVER contain business logic.

------------------------------------------------------------------------

### Functions

Functions must be:

-   Small
-   Focused
-   Testable
-   Real-world driven

One function = one responsibility.

------------------------------------------------------------------------

## 7. Database Design

### Riders

-   id
-   name
-   contact info
-   status
-   joined_at

### Bikes

-   id
-   model
-   registration
-   rider (FK)

### Rides

-   rider (FK)
-   date
-   distance
-   commission
-   status

Performance metrics must be computed, not duplicated.

------------------------------------------------------------------------

## 8. Security Standards

-   Use Django authentication
-   Hash everything sensitive
-   Environment variables for secrets
-   Proper permissions
-   Role-based access
-   Input validation everywhere

Never trust client data.

------------------------------------------------------------------------

## 9. Performance Rules

-   Avoid N+1 queries
-   Use select_related / prefetch_related
-   Cache expensive calculations
-   Paginate lists
-   Index foreign keys

Scalability is not optional.

------------------------------------------------------------------------

## 10. Logging & Monitoring

-   Centralized logging
-   Meaningful error messages
-   No silent failures
-   Structured logs
-   Exception tracking

------------------------------------------------------------------------

## 11. Final Enforcement

If code:

-   Is repeated → refactor
-   Is complex → simplify
-   Is unclear → rewrite
-   Is bloated → delete

Every line must justify its existence.

Clean code is a requirement --- not a preference.

------------------------------------------------------------------------

### Summary

This project prioritizes:

-   DRY architecture
-   Bootstrap-only UI
-   Service-driven backend
-   Secure JavaScript
-   Scalable Django patterns
-   Real-world practicality

Anything else is unacceptable.
