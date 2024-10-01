        print(Fore.MAGENTA + "Peringatan: Ini adalah nomor premium, mungkin dikenakan biaya tambahan.")
    else:
        print(Fore.MAGENTA + "Ini bukan nomor premium.")

    if timezones:
        print(Fore.MAGENTA + "Nomor ini terkait dengan zona waktu:", ", ".join(timezones))
    else:
        print(Fore.MAGENTA + "Tidak ada zona waktu yang terkait dengan nomor ini.")

    is_possible_as_mobile = phonenumbers.is_possible_number_for_type(mobileNo, PhoneNumberType.MOBILE)
    print(Fore.MAGENTA + "Mungkin sebagai Nomor Ponsel:", is_possible_as_mobile)

    has_extension = mobileNo.extension is not None
    print(Fore.MAGENTA + "Memiliki Extension:", has_extension)

    optimal_format = phonenumbers.format_by_pattern(mobileNo, phonenumbers.PhoneNumberFormat.INTERNATIONAL, [])
    print(Fore.MAGENTA + "Format Optimal:", optimal_format)

    is_valid_for_region = phonenumbers.is_valid_number_for_region(mobileNo, "ID")
    print(Fore.MAGENTA + "Valid untuk Region Indonesia:", is_valid_for_region)

    metadata = PhoneMetadata.load_all()
    print(Fore.MAGENTA + "Metadata Nomor Telepon Dimuat")

    print(Fore.MAGENTA + "Status Nomor: ")

    print(Fore.MAGENTA + "INI ADALAH NOMER TELPON")

except phonenumbers.NumberParseException as e:
    print(f"Kesalahan dalam memproses nomor: {e}")