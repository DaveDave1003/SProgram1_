def konvertor_men(castka, z_meny, na_menu, kurzy=None):
    vychozi_kurzy = {
        "CZK": 1.0,
        "EUR": 0.04,
        "USD": 0.043,
        "GBP": 0.034,
        "JPY": 6.43
    }

    if kurzy is None:
        kurzy = vychozi_kurzy

    if castka < 0 or z_meny not in kurzy or na_menu not in kurzy or kurzy[z_meny] == 0:
        return None

    czk = castka / kurzy[z_meny]
    vysledek = czk * kurzy[na_menu]
    return round(vysledek, 2)

print(konvertor_men(1000, "EUR", "CZK"))