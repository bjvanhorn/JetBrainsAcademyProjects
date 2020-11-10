spin, charge = input(), input()

if spin == "1":
    print("Photon Boson")
else:
    if charge == "-1/3":
        print("Strange Quark")
    elif charge == "2/3":
        print("Charm Quark")
    elif charge == "-1":
        print("Electron Lepton")
    else:
        print("Neutrino Lepton")
