def pick_resume(resumes):
    if not resumes:
        return None

    eliminate = "top"

    while len(resumes) > 1:
        midpoint = len(resumes) // 2

        if eliminate == "top":
            resumes = resumes[:midpoint]
            eliminate = "bottom"
        elif eliminate == "bottom":
            resumes = resumes[-midpoint:]
            eliminate = "top"

    return resumes[0]
