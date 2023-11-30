import tkinter as tk
import folium


class MapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("World Map with Information")

        self.map_center = [0, 0]
        self.create_map()

    def create_map(self):
        # Create a Folium map
        self.world_map = folium.Map(location=self.map_center, zoom_start=2)

        # Add a click event handler to the map
        self.world_map.add_child(folium.ClickForMarker(popup="Click me for information!"))

        # Create a frame to embed the Folium map in Tkinter
        self.map_frame = tk.Frame(self.root, width=800, height=600)
        self.map_frame.pack_propagate(0)
        self.map_frame.pack()

        # Embed the Folium map in Tkinter
        self.map_browser = folium.Macros("map", width=800, height=600)
        self.map_browser.map = self.world_map
        self.map_browser.parent = self.map_frame
        self.map_browser.pack(fill="both", expand=True)

        # Bind the click event to the map
        self.world_map.add_child(folium.ClickForMarker(popup=self.update_info_popup))

    def update_info_popup(self, location, **kwargs):
        # Display information about the clicked location (e.g., country name and population)
        coordinates = [location.latitude, location.longitude]
        popup_text = f"Coordinates: {coordinates}"

        # Add additional information based on the clicked location (you can customize this part)
        # For example, you can use reverse geocoding to get country information using services like Geonames or Nominatim.

        popup = folium.Popup(popup_text, max_width=300)
        marker = folium.Marker(coordinates, popup=popup)
        marker.add_to(self.world_map)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()