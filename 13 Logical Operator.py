is_age_gt_18 = True
has_no_criminal_rec = True

if is_age_gt_18 and has_no_criminal_rec:
    print("You are eligible for this job")
else:
    print("Sorry you are not eligible for this job")

    is_age_gt_18 = True
    has_no_criminal_rec = True

    if is_age_gt_18 or has_no_criminal_rec:
        print("You are eligible for this job")
    else:
        print("Sorry you are not eligible for this job")