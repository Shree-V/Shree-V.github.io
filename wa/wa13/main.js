// const TechStars = require('./tech_stars.json');

const TechStars = {
    "companyName" : "TechStars",
    "website" : "www.techstars.site",
    "employees" : 
    [ 
        {
            "name" : "Sam",
            "department" : "Tech",
            "designation" : "Manager",
            "salary" : 40000,
            "raise_eligible" : true,
            "wfh" : true
        },

        {
            "name" : "Mary",
            "department" : "Finance",
            "designation" : "Trainee",
            "salary" : 18500,
            "raise_eligible" : true,
            "wfh" : false
        },

        {
            "name" : "Bill",
            "department" : "HR",
            "designation" : "Executive",
            "salary" : 21200,
            "raise_eligible" : false,
            "wfh" : false
        },

        {
            "name" : "Anna",
            "department" : "Tech",
            "designation" : "Executive",
            "salary" : 25600,
            "raise_eligible" : false,
            "wfh" : true
        }

    ]
}

// Problem 1
for (let i = 0; i < 3; i++)
{
    console.log(TechStars.employees[i].name); 
}


// Problem 2
console.log('\n');
console.log(TechStars.companyName);
console.log(TechStars.website);
let len = TechStars.employees.length;
for (let i = 0; i < 3; i++)
{
    console.log(TechStars.employees[i].name);
} 

// Problem 3
console.log('\n');
console.log(TechStars.employees[3].name);

// Problem 4
console.log('\n');
let sum = 0;
for (let i = 0; i < TechStars.employees.length; i++)
{
    sum += TechStars.employees[i].salary;
}
console.log("Total Combined Salary:", sum);

// Problem 5
console.log('\n');
for (let i = 0; i < TechStars.employees.length; i++)
{
    if (TechStars.employees[i].raise_eligible == true)
    {
        console.log("Previous Salary:", TechStars.employees[i].salary);
        TechStars.employees[i].salary *= 1.1;
        console.log("Salary after Raise:" ,TechStars.employees[i].salary);
        TechStars.employees[i].raise_eligible = false;
    }
}

// Problem 6
console.log('\n');
for (let i = 0; i < TechStars.employees.length; i++)
{
    if (TechStars.employees[i].wfh == true)
    {
        console.log(TechStars.employees[i].name, "is working from home");
    }
    else if (TechStars.employees[i].wfh == false)
    {
        console.log(TechStars.employees[i].name, "is not working from home");
    }
}