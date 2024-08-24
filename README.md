# Commerce - Django Auction Site

This project is a Django-based auction site that allows users to create, view, and bid on auction listings. Users can also comment on listings and manage a watchlist of items they are interested in.

## Features

- **Filtering:** Users can filter auctions by tags or categories.
- **Watchlist:** Allows users to add items to a watchlist for easier tracking.
- **Adding Listing:** Users can create and list their own auctions.
- **User Registration:** Includes a user registration and authentication system.
- **Bidding Feature:** Users can place bids on items, with the highest bid winning the auction.
- **Commenting:** Users can leave comments on auction listings.

## Demo

Check out the [YouTube demo](https://www.youtube.com/watch?v=uriYljeqHgA) to see the project in action.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.10
- Django 3

### Installation

1. **Clone the repository**:


   git clone <repository_url>
   cd commerce
Create a virtual environment:

2. **Create a virtual environment:**:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies:

3. **Install the dependencies**:
pip install -r requirements.txt
Apply the migrations:

4. **Apply the migrations**:
python manage.py migrate
Run the development server:

5. **Run the development server**:
python manage.py runserver
