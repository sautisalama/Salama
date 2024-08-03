import numpy as np
from sklearn.neighbors import NearestNeighbors

# Sample data: [latitude, longitude, type_of_incident, urgency, availability]
service_providers = np.array([
    [1.2921, 36.8219, 1, 1, 1],
    [1.2951, 36.8220, 2, 1, 1],
    [1.2981, 36.8230, 3, 1, 1],
    # Add more providers
])

survivor = np.array([[1.3000, 36.8240, 1, 1, 1]])

# Fit the model
knn = NearestNeighbors(n_neighbors=3, metric='euclidean')
knn.fit(service_providers)

# Find the nearest service providers
distances, indices = knn.kneighbors(survivor)
