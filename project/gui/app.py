import customtkinter
from tkintermapview import TkinterMapView
from project.waze_api.route_calculator import RouteCalculator

customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    APP_NAME = "Distance and time calculator"
    WIDTH = 1200
    HEIGHT = 800

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.route_calculator = RouteCalculator("Bucharest, Romania", "BRNO,Czech Republic");
        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []
        self.selected_region = customtkinter.StringVar()
        self.REGIONS = ('US', 'EU', 'IL', 'AU')

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self, width=150

                                                 , corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_center = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_center.grid(row=0, column=1, rowspan=1, pady=0, padx=0, sticky="nsew")

        # self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        # self.frame_right.grid(row=0, column=2, rowspan=1, pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Set Marker",
                                                command=self.set_marker_event)
        self.button_1.grid(pady=(20, 0), padx=(20, 20), row=0, column=0)

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Clear Markers",
                                                command=self.clear_marker_event)
        self.button_2.grid(pady=(20, 0), padx=(20, 20), row=1, column=0)

        # self.button_3 = customtkinter.CTkButton(master=self.frame_left,
        #                                         text="Calculate",
        #                                         command=self.clear_marker_event)
        # self.button_3.grid(pady=(20, 0), padx=(20, 20), row=2, column=0)

        self.road_customization_label = customtkinter.CTkLabel(master=self.frame_left, text="Customize your trip",
                                                               anchor="w")
        self.road_customization_label.grid(pady=(20, 0), padx=(20, 20), row=2, column=0)

        # self.fuel_consumption = customtkinter.CTkLabel(master=self.frame_left, text="Fuel Consumption :")
        # self.fuel_consumption.grid(row=3, column=0, padx=(20, 20), pady=(20, 0))

        self.avoid_ferries = customtkinter.BooleanVar()
        self.checkbox_ferries = customtkinter.CTkCheckBox(master=self.frame_left, text="Avoid Ferries",
                                                          command=lambda: self.avoid_ferries.set(
                                                              not self.avoid_ferries.get()))
        self.checkbox_ferries.grid(row=3, column=0, padx=(20, 20), pady=(20, 0), sticky="w")

        self.avoid_toll_roads = customtkinter.BooleanVar()
        self.checkbox_toll_roads = customtkinter.CTkCheckBox(master=self.frame_left, text="Avoid Toll Roads",
                                                             command=lambda: self.avoid_toll_roads.set(
                                                                 not self.avoid_toll_roads.get()))
        self.checkbox_toll_roads.grid(row=4, column=0, padx=(20, 20), pady=(20, 0), sticky="w")

        self.avoid_subscription_roads = customtkinter.BooleanVar()
        self.checkbox_subscription_roads = customtkinter.CTkCheckBox(master=self.frame_left,
                                                                     text="Avoid Subscription Roads",
                                                                     command=lambda: self.avoid_subscription_roads.set(
                                                                         not self.avoid_subscription_roads.get()))

        self.checkbox_subscription_roads.grid(row=5, column=0, padx=(20, 20), pady=(20, 0), sticky="w")

        self.region_label = customtkinter.CTkCheckBox(master=self.frame_left,
                                                      text="Avoid Subscription Roads",
                                                      command=lambda: self.avoid_subscription_roads.set(
                                                          not self.avoid_subscription_roads.get()))

        self.checkbox_subscription_roads.grid(row=5, column=0, padx=(20, 20), pady=(20, 0), sticky="w")

        self.region_combobox = customtkinter.CTkComboBox(master=self.frame_left, values=self.REGIONS, width=60,
                                                         command=self.on_region_selected)
        self.region_combobox.grid(row=6, column=0, padx=(20, 20), pady=(20, 0), sticky="e")
        self.region_combobox.bind("<<ComboboxSelected>>", self.on_region_selected)

        self.region_label = customtkinter.CTkLabel(master=self.frame_left, text="Select Region",
                                                   anchor="w")
        self.region_label.grid(pady=(20, 0), padx=(20, 100), row=6, column=0)

        self.print_text = customtkinter.CTkTextbox(self.frame_left, wrap=customtkinter.WORD, height=120, width=200)
        self.print_text.grid(row=7, column=0, padx=(20, 20), pady=(20, 0), sticky="w")
        self.frame_left.grid_rowconfigure(8, weight=1)
        self.map_label = customtkinter.CTkLabel(self.frame_left, text="Tile Server:", anchor="w")
        self.map_label.grid(row=9, column=0, padx=(20, 20), pady=(20, 0))
        self.map_option_menu = customtkinter.CTkOptionMenu(self.frame_left, values=["OpenStreetMap", "Google normal",
                                                                                    "Google satellite"],
                                                           command=self.change_map)
        self.map_option_menu.grid(row=10, column=0, padx=(20, 20), pady=(10, 0))

        self.appearance_mode_label = customtkinter.CTkLabel(self.frame_left, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=11, column=0, padx=(20, 20), pady=(20, 0))
        self.appearance_mode_option_menu = customtkinter.CTkOptionMenu(self.frame_left,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode)
        self.appearance_mode_option_menu.grid(row=12, column=0, padx=(20, 20), pady=(10, 20))

        # # ============ frame_right ============

        self.frame_center.grid_rowconfigure(1, weight=1)
        self.frame_center.grid_rowconfigure(0, weight=0)
        self.frame_center.grid_columnconfigure(0, weight=1)
        self.frame_center.grid_columnconfigure(1, weight=0)
        self.frame_center.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_center, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0, columnspan=3, sticky="nswe", padx=(20, 20), pady=(20, 20))

        self.entry = customtkinter.CTkEntry(master=self.frame_center,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_center,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=2, sticky="w", padx=(12, 0), pady=12)

        # Set default values
        self.map_widget.set_address("Cluj Napoca")
        # self.map_option_menu.set("OpenStreetMap")
        # self.appearance_mode_option_menu.set("Dark")

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def set_marker_event(self):
        current_position = self.map_widget.get_position()
        self.marker_list.append(self.map_widget.set_marker(current_position[0], current_position[1]))

    def clear_marker_event(self):
        for marker in self.marker_list:
            marker.delete()

    def calculate_route(self):
        pass

    # def toggle_avoid_ferries(self):
    #     # todo
    #     pass
    #
    # def toggle_avoid_toll_roads(self):
    #     # todo
    #     pass
    #
    # def toggle_avoid_subscription_roads(self):
    #     # todo
    #     pass

    def on_region_selected(self, event):
        selected_value = self.region_combobox.get()
        print(selected_value)
        self.selected_region.set(selected_value)

        # Print the selected region in the Text widget
        self.print_text.insert(index=customtkinter.END, text=f"Selected Region: {selected_value}\n")

    @staticmethod
    def change_appearance_mode(new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_map(self, new_map: str):
        if new_map == "OpenStreetMap":
            self.map_widget.set_tile_server("https://a.tile.openstreetmap.org/{z}/{x}/{y}.png")
        elif new_map == "Google normal":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                            max_zoom=22)
        elif new_map == "Google satellite":
            self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga",
                                            max_zoom=22)

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
