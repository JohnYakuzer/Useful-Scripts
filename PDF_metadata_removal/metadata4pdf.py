import os
from PyPDF2 import PdfReader, PdfWriter

def main():
    print("--- PDF Metadata Cleaner ---")

    # Inputing PDF file location
    input_path = input("Unesite putanju do PDF fajla: ").strip()

    # Check to see if the file exists
    if not os.path.exists(input_path):
        print("Greska: Fajl ne postoji.")
        return

    # Loading file
    try:
        reader = PdfReader(input_path)
        writer = PdfWriter()

        # Copying all pages from the already existing file
        for page in reader.pages:
            writer.add_page(page)

        # Loading already available exif data
        existing_metadata = reader.metadata or {}
        print("\nPostojeći metapodaci:")
        for key, value in existing_metadata.items():
            print(f"  {key}: {value}")

        print("\nUnesite nove vrijednosti za metapodatke (ostavite prazno da preskočite):")

        # User input for new values for custom exif data
        new_metadata = {}
        fields = ["/Title", "/Author", "/Subject", "/Creator", "/Producer"]
        for field in fields:
            value = input(f"  {field[1:]}: ").strip()  # Prikazuje naziv polja bez kosih crta
            if value:
                new_metadata[field] = value

        # Writing new values to PDF
        writer.add_metadata(new_metadata)

        # Saving the file at already existing location with the already inputed PDF file
        output_path = os.path.join(os.path.dirname(input_path), "metadata_clean.pdf")
        with open(output_path, "wb") as output_file:
            writer.write(output_file)

        print(f"\nNovi fajl sa izmijenjenim metapodacima je sacuvan kao: {output_path}")

    except Exception as e:
        print(f"Greska prilikom obrade fajla: {e}")

if __name__ == "__main__":
    main()

