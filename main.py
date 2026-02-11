def main():
    print("Hello from test-osa!")
    from lab_devices import Yeni

    try:
        osa = Yeni(
            resource_address = 'TCPIP0::192.168.54.1::5025::SOCKET',
        )
    except Exception as e:
        raise ConnectionError(f"Could not connect to OSA:\n {e}")

    osa_idn = osa.id
        # osa.wait_for()
    print("Instrument ID:", osa_idn)

    


if __name__ == "__main__":
    main()
