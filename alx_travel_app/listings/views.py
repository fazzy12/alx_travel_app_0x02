from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


class ListingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting property Listings.
    Allows read access (GET) to all users and requires authentication 
    for CUD (Create, Update, Delete) operations.
    """
    queryset = Listing.objects.all().order_by('-created_at')
    serializer_class = ListingSerializer
    # Allows read access to all, but requires authentication for CUD operations
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Set the host_id to the authenticated user making the request upon creation."""
        serializer.save(host_id=self.request.user)


class BookingViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, creating, updating, and deleting Bookings.
    Requires authentication (IsAuthenticated) for all operations.
    """
    # Note: In a production app, the queryset should be filtered to show only 
    # bookings relevant to the current user (guest or host).
    queryset = Booking.objects.all().order_by('-created_at')
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        """Set the user_id (guest) to the authenticated user making the booking."""
        serializer.save(user_id=self.request.user)