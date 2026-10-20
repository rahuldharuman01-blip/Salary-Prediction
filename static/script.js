const form = document.getElementById("salaryForm");

form.addEventListener("submit", function (event) {
    event.preventDefault();

    // Get input values
    const jobrole = document.getElementById("jobrole").value;
    const experience = document.getElementById("experience").value;
    const location = document.getElementById("location").value;
    const education = document.getElementById("education").value;

    // Check whether all fields are filled
    if (!jobrole || !experience || !location || !education) {
        alert("Please fill all the fields.");
        return;
    }

    // UI only - no prediction
    alert("Your details have been submitted successfully.");

    console.log("Job Role:", jobrole);
    console.log("Experience:", experience);
    console.log("Location:", location);
    console.log("Education:", education);
});