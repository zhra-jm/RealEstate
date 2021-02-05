from profile import ApartmentPurchasable, ApartmentRental, HousePurchasable, HouseRental

SUPERVISOR_CREDENTIALS = [
    {'username': 'admin', 'password': '123'}
]

AGENTS_FILE_PATH = "E:\\zahra\\Python_nimz\\Real estate advisor\\agent.jason"

PROFILE_MAPPER = {
    ('house', 'purchase'): HousePurchasable,
    ('house', 'rent'): HouseRental,
    ('apartment', 'purchase'): ApartmentPurchasable,
    ('apartment', 'rent'): ApartmentRental
}