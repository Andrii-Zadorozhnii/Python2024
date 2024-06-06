good_or_not_good = input("Type good or not good. ")
army_size = input("Is it army of 1,2 or 3? ")
match good_or_not_good:
    case "good":
        match army_size:
            case 1:
                print("good 1")
            case 2:
                print("good 2")
            case 3:
                print("good 3")
    case "not good":
        match army_size:
            case 1:
                print("good 1")
            case 2:
                print("good 2")
            case 3:
                print("good 3")
        print("not good")