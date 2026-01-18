function updateSubjects() {
  const subjects = {
    // School Classes
    'class1': ['English', 'Mathematics', 'Science', 'Environmental Studies', 'Other'],
    'class2': ['English', 'Mathematics', 'Science', 'Environmental Studies', 'Other'],
    'class3': ['English', 'Mathematics', 'Science', 'Environmental Studies', 'Other'],
    'class4': ['English', 'Mathematics', 'Science', 'Environmental Studies', 'Other'],
    'class5': ['English', 'Mathematics', 'Science', 'Environmental Studies', 'Other'],
    'class6': ['Mathematics', 'Science', 'English', 'Social Studies', 'Hindi', 'Other'],
    'class7': ['Mathematics', 'Science', 'English', 'Social Studies', 'Hindi', 'Other'],
    'class8': ['Mathematics', 'Science', 'English', 'Social Studies', 'Hindi', 'Computer Science', 'Other'],
    'class9': ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English', 'Other'],
    'class10': ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'English', 'Other'],
    'class11': ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', 'Other'],
    'class12': ['Physics', 'Chemistry', 'Mathematics', 'Biology', 'English', 'Other'],
  
    // Engineering Branches
    'computer_engineering': ['Data Structures', 'Algorithms', 'Operating Systems', 'Databases', 'Computer Networks', 'Other'],
    'mechanical_engineering': ['Thermodynamics', 'Mechanics', 'Fluid Dynamics', 'Machine Design', 'Manufacturing Processes', 'Other'],
    'electrical_engineering': ['Circuits and Systems', 'Control Systems', 'Power Systems', 'Signal Processing', 'Electromagnetics', 'Other'],
    'civil_engineering': ['Structural Analysis', 'Concrete Technology', 'Geotechnical Engineering', 'Transportation Engineering', 'Water Resources', 'Other'],
    'electronics_engineering': ['Analog Circuits', 'Digital Circuits', 'Microprocessors', 'VLSI Design', 'Embedded Systems', 'Other'],
   
    // Other Courses
    'business_management': ['Marketing', 'Finance', 'Human Resource Management', 'Operations Management', 'Strategic Management', 'Other'],
    'medicine': ['Anatomy', 'Physiology', 'Pharmacology', 'Pathology', 'Surgery', 'Other'],
    'law': ['Constitutional Law', 'Criminal Law', 'Civil Law', 'Corporate Law', 'International Law', 'Other'],
    'architecture': ['Design Principles', 'Building Materials', 'Structural Systems', 'Urban Planning', 'Sustainable Design', 'Other'],
    'arts': ['History', 'Philosophy', 'Political Science', 'Sociology', 'Psychology', 'Other'],
   
  
    // Other Value Options
    'Technology': ['Programming', 'Web Development', 'Data Analysis', 'AI & ML', 'Cloud Computing', 'Other'],
    
    'Science': ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Botany', 'Geology', 'Engineering Drawing'],
    'Arts': ['History', 'Geography', 'Political Science', 'Sociology', 'Psychology', 'Philosophy', 'Human Rights and Gender Science', 'Public Administration', 'Home Science', 'others.'],
    'Commerce': ['Accountancy', 'Business Studies', 'Economics', 'Legal Studies', 'Entrepreneurship'],
    
    'CompetitiveExams': ['JEE Mains', 'JEE Advanced', 'NEET', 'CAT', 'MAT', 'CMAT', 'GATE', 'CLAT', 'and others'],
    
    'LanguageClasses': ['Hindi', 'English', 'Sanskrit','German', 'French', 'Spanish','others.'],

  
    
    'ProgrammingLanguages': ['Python', 'Java', 'C++', 'JavaScript', '.NET Training', 'C Language', 'PHP', 'others'],
    
    'ITTrainingCourses': ['Microsoft Office', 'SAP', 'Selenium', 'AWS', 'Data Science', 'Adobe Photoshop', 'DevOps', 'Web Designing', 'App Development', 'Angular.js', 'and more'],
    
    'InternationalExams': ['IELTS Coaching', 'PTE Academic Exam Coaching', 'GRE', 'GMAT', 'TOEFL', 'and other international competitive exams'],
    
    'DegreeCourses': ['BA', 'B.Sc', 'B.Com', 'BBA', 'BCA', 'MA', 'M.Com', 'B.Tech', 'B.Arch', 'MBA', 'LLB', 'other'] ,
    'Others': [ 'Other'],
  };
  
  
    const selectedClass = document.getElementById('class_of_study').value;
    const subjectSelectionDiv = document.getElementById('subject-selection');
    
    // Clear the previous subjects
    subjectSelectionDiv.innerHTML = '';
    
    if (!selectedClass) return;
  
    const subjectList = subjects[selectedClass] || [];
    
    // Add subjects as checkboxes
    subjectList.forEach(function(subject) {
      subjectSelectionDiv.innerHTML += `
        <div class="form-check">
          <input class="form-check-input" type="checkbox" name="subjects" value="${subject}" id="${subject}">
          <label class="form-check-label" for="${subject}">
            ${subject}
          </label>
        </div>
      `;
    });
  }
  function handleFormSubmit(event) {
    const selectedSubjects = document.querySelectorAll('input[name="subjects"]:checked');
    
    if (selectedSubjects.length === 0) {
      alert("Please select at least one subject.");
      event.preventDefault(); // Prevent form submission
      return;
    }
  
    alert("Form submitted successfully!");
  }
  
 