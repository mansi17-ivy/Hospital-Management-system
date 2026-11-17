# Project Summary & Reflection

## Overview
This project implements a foundational Hospital Management System in Python to simulate real-world data tracking and menu-driven user interaction.

## Difficulties Faced & Solutions
1. **Handling Invalid User Inputs (Type Errors):** 
   * *Problem:* When users entered letters instead of numbers for age or ID choices, the program crashed.
   * *Solution:* Implemented `try-except` blocks with `ValueError` handling to catch invalid inputs gracefully and prompt the user again without crashing.
2. **Data Structure Organization:**
   * *Problem:* Keeping track of multiple patients and appointments simultaneously.
   * *Solution:* Used Python lists and dictionaries to store records cleanly in memory during runtime.

## Test Cases & Execution
* **Test Case 1 (Valid Patient Registration):** Entering correct names and ages successfully adds the patient to the system record.
* **Test Case 2 (Invalid Input Handling):** Entering strings for numeric fields successfully triggers error handling messages.
