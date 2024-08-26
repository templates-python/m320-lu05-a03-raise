from gradelist import GradeList


def main():
    demo = GradeList()
    demo.add_grade(4.5)
    demo.add_grade(5.0)
    demo.add_grade(3.5)
    demo.add_grade(4.0)
    demo.add_grade(4.5)
    print(demo)
    # und einen nächsten Wert einfügen, der zu einem Overflow führen wird.
    print("\nund nun einen weiteren Wert zufügen")
    demo.add_grade(3.5)
    print(demo)

    print("\nLösche Wert an 2. Stelle")
    demo.remove_grade(1)  # Index beginnt bei 0
    print(demo)

    # und nun einen Wert zufügen der eine ungültige Note darstellt.
    print("\nund nun eine ungültige Note zufügen")
    demo.add_grade(7.0)
    print(demo)

    # und nun einen Wert an einer Stelle lesen, die es nicht gibt
    print("\nNote an Position 8 lesen ")
    print(demo.take_grade(8))

    print(f"\nListe umfasst zur Zeit {demo.current_grade_count} Noten")
    print(f"Note an 3. Stelle ist {demo.take_grade(2)}")
    print(f"Grösse der Liste beträgt {demo.max_grade_count}\n")
    print(demo)


if __name__ == '__main__':
    main()