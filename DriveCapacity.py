print("Hard drive code goes here")
# CSC333 - Hard Drive Capacity Calculator

def main():
    # Prompting for user input
    platters = int(input("Enter the number of platters: "))
    surfaces = int(input("Enter the number of surfaces per platter: "))
    tracks = int(input("Enter the number of tracks per surface: "))
    sectors = int(input("Enter the number of sectors per track: "))
    bytes_per_sector = int(input("Enter the number of bytes per sector: "))

    # Total bytes calculation
    total_bytes = platters * surfaces * tracks * sectors * bytes_per_sector

    # Conversion to higher units
    kb = total_bytes / 1024
    mb = kb / 1024
    gb = mb / 1024
    tb = gb / 1024

    # Decide the smallest unit > 1.0 and print with 1 decimal place
    if tb > 1.0:
        print(f"Drive capacity: {tb:.1f} TB")
    elif gb > 1.0:
        print(f"Drive capacity: {gb:.1f} GB")
    elif mb > 1.0:
        print(f"Drive capacity: {mb:.1f} MB")
    elif kb > 1.0:
        print(f"Drive capacity: {kb:.1f} KB")
    else:
        print(f"Drive capacity: {total_bytes} Bytes")


main()
