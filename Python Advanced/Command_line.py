import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--Physics", help="Physics results")
    parser.add_argument("--Maths", help="Maths results")
    parser.add_argument("--Geometry", help="Geometrys results")
    parser.add_argument("--Chemistry", help="Chemistrys results")

    args = parser.parse_args()

    print(args.Physics)
    print(args.Maths)
    print(args.Geometry)
    print(args.Chemistry)

    p = int(args.Physics)
    m = int(args.Maths)
    g = int(args.Geometry)
    c = int(args.Chemistry)

    result = (p+m+g+c)/4

    print("Μέσος Όρος Μαθημάτων Κατεύθυνσης:",result)

