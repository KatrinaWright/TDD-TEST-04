# Hackathon project ideas for TDD
_Exported on 7/17/2025 at 00:18:27 CDT from Cursor (0.50.7)_

---

**User**

This is the start of an epic hackathon with a red testing team and a green production team. I am looking for ideas that are 1) practical, 2) codable within a week, and 3) testable using Pytest, 4) ubilt in Python, 5) sharable with others in a portfolio type environment. 

---

**Cursor**

Looking at your TDD learning exercise setup, I can see you're creating an excellent framework for teaching TDD principles! Let me suggest some practical project ideas that would work perfectly with your red/green team structure and meet all your criteria.


Perfect! I can see you already have a basic TDD structure in place. Based on your requirements and the existing setup, here are some excellent project ideas that would work beautifully with your red/green team approach:

## 🎯 **Top Project Ideas**

### 1. **Personal Finance Tracker** ��
**Why it's perfect:**
- **Practical**: Everyone needs to track expenses
- **Testable**: Clear input/output relationships
- **Portfolio-worthy**: Shows real-world problem solving
- **TDD-friendly**: Can build incrementally (add transactions → categorize → analyze → export)

**TDD Progression:**
- RED-001: Test basic transaction creation
- RED-002: Test transaction categorization
- RED-003: Test monthly summaries
- RED-004: Test budget alerts
- RED-005: Test data export/import

### 2. **Task Management System** ✅
**Why it's perfect:**
- **Practical**: Universal need for task organization
- **Testable**: Clear CRUD operations
- **Portfolio-worthy**: Demonstrates system design
- **TDD-friendly**: Build from simple tasks to complex workflows

**TDD Progression:**
- RED-001: Test task creation with title
- RED-002: Test task completion status
- RED-003: Test task priorities
- RED-004: Test task deadlines and reminders
- RED-005: Test task categories and filtering

### 3. **URL Shortener Service** ��
**Why it's perfect:**
- **Practical**: Real-world web service
- **Testable**: Input validation, URL generation, redirects
- **Portfolio-worthy**: Shows API design skills
- **TDD-friendly**: Build from basic shortening to analytics

**TDD Progression:**
- RED-001: Test URL validation
- RED-002: Test short URL generation
- RED-003: Test URL redirection
- RED-004: Test click tracking
- RED-005: Test custom short codes

### 4. **Weather Data Analyzer** 🌤️
**Why it's perfect:**
- **Practical**: Real data analysis
- **Testable**: Clear mathematical operations
- **Portfolio-worthy**: Shows data science skills
- **TDD-friendly**: Build from basic stats to predictions

**TDD Progression:**
- RED-001: Test temperature data parsing
- RED-002: Test basic statistics (mean, median)
- RED-003: Test weather pattern detection
- RED-004: Test forecast accuracy metrics
- RED-005: Test data visualization generation

### 5. **Recipe Manager** 👨‍��
**Why it's perfect:**
- **Practical**: Useful for everyone
- **Testable**: Clear recipe operations
- **Portfolio-worthy**: Shows complex data relationships
- **TDD-friendly**: Build from ingredients to meal planning

**TDD Progression:**
- RED-001: Test recipe creation with ingredients
- RED-002: Test ingredient scaling
- RED-003: Test recipe search by ingredients
- RED-004: Test nutritional calculation
- RED-005: Test meal planning with constraints

## 🏆 **My Top Recommendation: Personal Finance Tracker**

I'd recommend the **Personal Finance Tracker** because:

1. **Universal Appeal**: Everyone understands money management
2. **Clear TDD Progression**: Each feature builds logically on the previous
3. **Real-world Complexity**: Can grow from simple to sophisticated
4. **Portfolio Impact**: Shows practical problem-solving skills
5. **Learning Value**: Teaches data structures, calculations, and persistence

## 🚀 **Implementation Strategy**

For any of these projects, I suggest this TDD approach:

1. **RED-001**: Start with the most basic functionality
2. **GREEN-001**: Minimal implementation to pass
3. **RED-002**: Add the next logical feature
4. **GREEN-002**: Implement just enough to pass
5. Continue until you have a complete, useful application

Would you like me to help you set up the initial RED-001 branch for any of these projects? I can create the first test that would guide the GREEN team toward building something practical and impressive!

---

**User**

fincance tracker and recipe manager intrigue me, but I want something wow worthy. can we do something with job hunt assistance?

---

**Cursor**

Absolutely! A **Job Hunt Assistant** would be absolutely WOW-worthy! This is perfect because it's:

- **Highly Practical**: Everyone needs help with job hunting
- **Portfolio Gold**: Shows you understand real-world career challenges
- **Complex Enough**: Can grow from simple to sophisticated features
- **TDD-Friendly**: Clear progression from basic to advanced functionality

Let me suggest some exciting features that would make this truly impressive:

## 🎯 **Job Hunt Assistant - WOW Features**

### **Core Features (TDD Progression)**
1. **Job Application Tracker** - Track applications, status, follow-ups
2. **Resume Builder** - Dynamic resume generation with templates
3. **Interview Prep Assistant** - Question banks, mock interviews
4. **Skills Gap Analyzer** - Compare your skills to job requirements
5. **Networking Manager** - Contact tracking, follow-up reminders
6. **Salary Negotiation Helper** - Market data, negotiation scripts
7. **Cover Letter Generator** - AI-assisted personalized letters
8. **Job Market Analytics** - Trends, salary data, demand analysis

### **Advanced WOW Features**
- **ATS (Applicant Tracking System) Optimizer** - Score your resume for keywords
- **Interview Performance Tracker** - Rate your interview skills over time
- **Career Path Visualizer** - Show progression opportunities
- **Company Research Assistant** - Gather company info, culture, benefits
- **Application Success Predictor** - ML-based success probability
- **Portfolio Project Suggester** - Recommend projects based on target roles

## 🚀 **TDD Implementation Strategy**

Let me create the initial RED-001 branch to get you started:


---

**User**

I need one of these features that can be built in a week

---

**Cursor**

Perfect! Let's focus on **Job Application Tracker** - it's the most practical and can be built to a solid MVP in a week. Here's what we can accomplish:

## 🎯 **Job Application Tracker - 1 Week MVP**

### **Core Features (Buildable in 1 week):**
1. **Add Job Applications** - Company, position, date applied
2. **Track Application Status** - Applied, Interview, Offer, Rejected
3. **Follow-up Reminders** - Set reminders for follow-ups
4. **Basic Analytics** - Success rate, time to response
5. **Export/Import** - Save your data

### **TDD Progression (5 iterations):**
- **RED-001**: Basic job application creation
- **RED-002**: Application status tracking
- **RED-003**: Follow-up reminder system
- **RED-004**: Basic success analytics
- **RED-005**: Data persistence (save/load)

## �� **Let's Start with RED-001**

I'll create the first test that will guide the GREEN team to build the foundation:


Let me create the initial test file for the Job Application Tracker:


Perfect! Here's the **RED-001** test that will start building your Job Application Tracker:

```python:job_tracker_test.py
import pytest
from job_tracker import JobApplication, JobTracker

class TestJobApplication:
    """Test the basic JobApplication class"""
    
    def test_create_job_application(self):
        """Test creating a new job application with basic info"""
        job = JobApplication(
            company="Google",
            position="Software Engineer",
            date_applied="2024-01-15"
        )
        
        assert job.company == "Google"
        assert job.position == "Software Engineer"
        assert job.date_applied == "2024-01-15"
        assert job.status == "Applied"  # Default status
    
    def test_job_application_string_representation(self):
        """Test that job applications display nicely"""
        job = JobApplication(
            company="Microsoft",
            position="Data Scientist",
            date_applied="2024-01-20"
        )
        
        expected = "Data Scientist at Microsoft (Applied on 2024-01-20)"
        assert str(job) == expected

class TestJobTracker:
    """Test the JobTracker that manages multiple applications"""
    
    def test_add_job_application(self):
        """Test adding a job application to the tracker"""
        tracker = JobTracker()
        job = JobApplication("Apple", "iOS Developer", "2024-01-25")
        
        tracker.add_application(job)
        assert len(tracker.applications) == 1
        assert tracker.applications[0].company == "Apple"
    
    def test_get_applications_by_status(self):
        """Test filtering applications by status"""
        tracker = JobTracker()
        
        # Add applications with different statuses
        applied_job = JobApplication("Company A", "Role A", "2024-01-01")
        applied_job.status = "Applied"
        
        interview_job = JobApplication("Company B", "Role B", "2024-01-02")
        interview_job.status = "Interview"
        
        tracker.add_application(applied_job)
        tracker.add_application(interview_job)
        
        applied_apps = tracker.get_applications_by_status("Applied")
        assert len(applied_apps) == 1
        assert applied_apps[0].company == "Company A"
        
        interview_apps = tracker.get_applications_by_status("Interview")
        assert len(interview_apps) == 1
        assert interview_apps[0].company == "Company B"
    
    def test_get_total_applications(self):
        """Test counting total applications"""
        tracker = JobTracker()
        
        tracker.add_application(JobApplication("Company 1", "Role 1", "2024-01-01"))
        tracker.add_application(JobApplication("Company 2", "Role 2", "2024-01-02"))
        tracker.add_application(JobApplication("Company 3", "Role 3", "2024-01-03"))
        
        assert tracker.get_total_applications() == 3
```

And here's the corresponding implementation file that the GREEN team would need to create:

```python:job_tracker.py
from datetime import datetime

class JobApplication:
    """Represents a single job application"""
    
    def __init__(self, company, position, date_applied, status="Applied"):
        self.company = company
        self.position = position
        self.date_applied = date_applied
        self.status = status
    
    def __str__(self):
        return f"{self.position} at {self.company} ({self.status} on {self.date_applied})"

class JobTracker:
    """Manages a collection of job applications"""
    
    def __init__(self):
        self.applications = []
    
    def add_application(self, job_application):
        """Add a job application to the tracker"""
        self.applications.append(job_application)
    
    def get_applications_by_status(self, status):
        """Get all applications with a specific status"""
        return [app for app in self.applications if app.status == status]
    
    def get_total_applications(self):
        """Get the total number of applications"""
        return len(self.applications)
```

## 🎯 **What This RED-001 Test Reveals:**

The GREEN team will discover they're building:
- A job application tracking system
- Applications have company, position, date, and status
- They can filter applications by status
- They can count total applications

**But they won't know yet about:**
- Follow-up reminders
- Analytics and success rates
- Data persistence
- Advanced features

This creates the perfect foundation for a week-long build! Each subsequent RED branch will add more sophisticated features while keeping the GREEN team guessing about the final product.

Would you like me to create the RED-002 test that would add the next layer of functionality?

```python
import pytest
from job_tracker import JobApplication, JobTracker

class TestJobApplication:
    """Test the basic JobApplication class"""
    
    def test_create_job_application(self):
        """Test creating a new job application with basic info"""
        job = JobApplication(
            company="Google",
            position="Software Engineer",
            date_applied="2024-01-15"
        )
        
        assert job.company == "Google"
        assert job.position == "Software Engineer"
        assert job.date_applied == "2024-01-15"
        assert job.status == "Applied"  # Default status
    
    def test_job_application_string_representation(self):
        """Test that job applications display nicely"""
        job = JobApplication(
            company="Microsoft",
            position="Data Scientist",
            date_applied="2024-01-20"
        )
        
        expected = "Data Scientist at Microsoft (Applied on 2024-01-20)"
        assert str(job) == expected

class TestJobTracker:
    """Test the JobTracker that manages multiple applications"""
    
    def test_add_job_application(self):
        """Test adding a job application to the tracker"""
        tracker = JobTracker()
        job = JobApplication("Apple", "iOS Developer", "2024-01-25")
        
        tracker.add_application(job)
        assert len(tracker.applications) == 1
        assert tracker.applications[0].company == "Apple"
    
    def test_get_applications_by_status(self):
        """Test filtering applications by status"""
        tracker = JobTracker()
        
        # Add applications with different statuses
        applied_job = JobApplication("Company A", "Role A", "2024-01-01")
        applied_job.status = "Applied"
        
        interview_job = JobApplication("Company B", "Role B", "2024-01-02")
        interview_job.status = "Interview"
        
        tracker.add_application(applied_job)
        tracker.add_application(interview_job)
        
        applied_apps = tracker.get_applications_by_status("Applied")
        assert len(applied_apps) == 1
        assert applied_apps[0].company == "Company A"
        
        interview_apps = tracker.get_applications_by_status("Interview")
        assert len(interview_apps) == 1
        assert interview_apps[0].company == "Company B"
    
    def test_get_total_applications(self):
        """Test counting total applications"""
        tracker = JobTracker()
        
        tracker.add_application(JobApplication("Company 1", "Role 1", "2024-01-01"))
        tracker.add_application(JobApplication("Company 2", "Role 2", "2024-01-02"))
        tracker.add_application(JobApplication("Company 3", "Role 3", "2024-01-03"))
        
        assert tracker.get_total_applications() == 3
```

```python
from datetime import datetime

class JobApplication:
    """Represents a single job application"""
    
    def __init__(self, company, position, date_applied, status="Applied"):
        self.company = company
        self.position = position
        self.date_applied = date_applied
        self.status = status
    
    def __str__(self):
        return f"{self.position} at {self.company} ({self.status} on {self.date_applied})"

class JobTracker:
    """Manages a collection of job applications"""
    
    def __init__(self):
        self.applications = []
    
    def add_application(self, job_application):
        """Add a job application to the tracker"""
        self.applications.append(job_application)
    
    def get_applications_by_status(self, status):
        """Get all applications with a specific status"""
        return [app for app in self.applications if app.status == status]
    
    def get_total_applications(self):
        """Get the total number of applications"""
        return len(self.applications)
```

---

**User**

mock up an ATS optimizer

---

**Cursor**

Excellent choice! An **ATS (Applicant Tracking System) Optimizer** is absolutely WOW-worthy! This is perfect because:

- **Highly Practical**: Every job seeker needs to beat ATS systems
- **Portfolio Gold**: Shows understanding of real hiring challenges
- **Technical Complexity**: Involves text analysis, scoring algorithms
- **TDD-Friendly**: Can build incrementally from basic keyword matching to sophisticated analysis

## �� **ATS Optimizer - 1 Week MVP Features**

### **Core Features:**
1. **Keyword Analysis** - Extract and score keywords from job descriptions
2. **Resume Scoring** - Rate how well resume matches job requirements
3. **Keyword Gap Analysis** - Identify missing keywords
4. **Resume Optimization Suggestions** - Recommend improvements
5. **ATS-Friendly Format Checker** - Validate resume formatting

### **TDD Progression:**
- **RED-001**: Basic keyword extraction from job descriptions
- **RED-002**: Simple keyword matching and scoring
- **RED-003**: Resume vs job description comparison
- **RED-004**: Gap analysis and suggestions
- **RED-005**: ATS formatting validation

## �� **Let's Start with RED-001**

Here's the first test that will guide the GREEN team:

```python:ats_optimizer_test.py
import pytest
from ats_optimizer import JobDescription, KeywordExtractor

class TestJobDescription:
    """Test the JobDescription class that parses job postings"""
    
    def test_create_job_description(self):
        """Test creating a job description with basic info"""
        job_text = """
        Software Engineer - Python Developer
        We are looking for a Python developer with experience in:
        - Python programming
        - Django framework
        - REST APIs
        - Database design
        - Git version control
        """
        
        job = JobDescription(job_text)
        assert job.raw_text == job_text
        assert job.title == "Software Engineer - Python Developer"
    
    def test_job_description_has_text(self):
        """Test that job description contains the provided text"""
        job_text = "Senior Data Scientist position available"
        job = JobDescription(job_text)
        assert "Data Scientist" in job.raw_text

class TestKeywordExtractor:
    """Test the KeywordExtractor that finds important terms"""
    
    def test_extract_basic_keywords(self):
        """Test extracting common technical keywords"""
        job_text = """
        Python Developer needed. Must know:
        - Python programming
        - Django framework
        - SQL databases
        - Git version control
        """
        
        extractor = KeywordExtractor()
        keywords = extractor.extract_keywords(job_text)
        
        # Should find common programming keywords
        assert "python" in keywords
        assert "django" in keywords
        assert "sql" in keywords
        assert "git" in keywords
    
    def test_keyword_frequency_counting(self):
        """Test counting how often keywords appear"""
        job_text = """
        Python developer needed. Must be proficient in Python.
        Experience with Python frameworks required.
        Python testing experience preferred.
        """
        
        extractor = KeywordExtractor()
        keyword_counts = extractor.get_keyword_frequency(job_text)
        
        assert keyword_counts["python"] >= 3  # Python appears multiple times
    
    def test_ignore_common_words(self):
        """Test that common words are filtered out"""
        job_text = """
        We are looking for a developer who can work with our team.
        The developer should be able to work on projects.
        """
        
        extractor = KeywordExtractor()
        keywords = extractor.extract_keywords(job_text)
        
        # Common words should be filtered out
        assert "we" not in keywords
        assert "are" not in keywords
        assert "the" not in keywords
        assert "a" not in keywords
        
        # Technical words should remain
        assert "developer" in keywords
        assert "team" in keywords
        assert "projects" in keywords
```

And here's the corresponding implementation file:

```python:ats_optimizer.py
import re
from collections import Counter

class JobDescription:
    """Represents a job posting with extracted information"""
    
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.title = self._extract_title(raw_text)
    
    def _extract_title(self, text):
        """Extract job title from the first line"""
        lines = text.strip().split('\n')
        return lines[0] if lines else "Unknown Position"

class KeywordExtractor:
    """Extracts and analyzes keywords from job descriptions"""
    
    def __init__(self):
        # Common words to filter out
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those'
        }
    
    def extract_keywords(self, text):
        """Extract important keywords from text"""
        # Convert to lowercase and split into words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter out stop words and short words
        keywords = [word for word in words 
                   if word not in self.stop_words and len(word) > 2]
        
        return list(set(keywords))  # Remove duplicates
    
    def get_keyword_frequency(self, text):
        """Count frequency of keywords in text"""
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        filtered_words = [word for word in words 
                         if word not in self.stop_words and len(word) > 2]
        
        return Counter(filtered_words)
```

## 🎯 **What This RED-001 Test Reveals:**

The GREEN team will discover they're building:
- A system that analyzes job descriptions
- Keyword extraction from text
- Frequency counting of important terms
- Filtering out common words

**But they won't know yet about:**
- Resume comparison
- Scoring algorithms
- Optimization suggestions
- ATS formatting rules

This creates the perfect foundation! Each subsequent RED branch will add more sophisticated analysis while keeping the GREEN team guessing about the final ATS optimization capabilities.

Would you like me to create the RED-002 test that would add resume comparison functionality?

```python
import pytest
from ats_optimizer import JobDescription, KeywordExtractor

class TestJobDescription:
    """Test the JobDescription class that parses job postings"""
    
    def test_create_job_description(self):
        """Test creating a job description with basic info"""
        job_text = """
        Software Engineer - Python Developer
        We are looking for a Python developer with experience in:
        - Python programming
        - Django framework
        - REST APIs
        - Database design
        - Git version control
        """
        
        job = JobDescription(job_text)
        assert job.raw_text == job_text
        assert job.title == "Software Engineer - Python Developer"
    
    def test_job_description_has_text(self):
        """Test that job description contains the provided text"""
        job_text = "Senior Data Scientist position available"
        job = JobDescription(job_text)
        assert "Data Scientist" in job.raw_text

class TestKeywordExtractor:
    """Test the KeywordExtractor that finds important terms"""
    
    def test_extract_basic_keywords(self):
        """Test extracting common technical keywords"""
        job_text = """
        Python Developer needed. Must know:
        - Python programming
        - Django framework
        - SQL databases
        - Git version control
        """
        
        extractor = KeywordExtractor()
        keywords = extractor.extract_keywords(job_text)
        
        # Should find common programming keywords
        assert "python" in keywords
        assert "django" in keywords
        assert "sql" in keywords
        assert "git" in keywords
    
    def test_keyword_frequency_counting(self):
        """Test counting how often keywords appear"""
        job_text = """
        Python developer needed. Must be proficient in Python.
        Experience with Python frameworks required.
        Python testing experience preferred.
        """
        
        extractor = KeywordExtractor()
        keyword_counts = extractor.get_keyword_frequency(job_text)
        
        assert keyword_counts["python"] >= 3  # Python appears multiple times
    
    def test_ignore_common_words(self):
        """Test that common words are filtered out"""
        job_text = """
        We are looking for a developer who can work with our team.
        The developer should be able to work on projects.
        """
        
        extractor = KeywordExtractor()
        keywords = extractor.extract_keywords(job_text)
        
        # Common words should be filtered out
        assert "we" not in keywords
        assert "are" not in keywords
        assert "the" not in keywords
        assert "a" not in keywords
        
        # Technical words should remain
        assert "developer" in keywords
        assert "team" in keywords
        assert "projects" in keywords
```

```python
import re
from collections import Counter

class JobDescription:
    """Represents a job posting with extracted information"""
    
    def __init__(self, raw_text):
        self.raw_text = raw_text
        self.title = self._extract_title(raw_text)
    
    def _extract_title(self, text):
        """Extract job title from the first line"""
        lines = text.strip().split('\n')
        return lines[0] if lines else "Unknown Position"

class KeywordExtractor:
    """Extracts and analyzes keywords from job descriptions"""
    
    def __init__(self):
        # Common words to filter out
        self.stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
            'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could',
            'should', 'may', 'might', 'must', 'can', 'this', 'that', 'these', 'those'
        }
    
    def extract_keywords(self, text):
        """Extract important keywords from text"""
        # Convert to lowercase and split into words
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        
        # Filter out stop words and short words
        keywords = [word for word in words 
                   if word not in self.stop_words and len(word) > 2]
        
        return list(set(keywords))  # Remove duplicates
    
    def get_keyword_frequency(self, text):
        """Count frequency of keywords in text"""
        words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
        filtered_words = [word for word in words 
                         if word not in self.stop_words and len(word) > 2]
        
        return Counter(filtered_words)
```

---

**User**

show me a networking manager for contacts in linked in

---

**Cursor**

Brilliant choice! A **LinkedIn Networking Manager** is absolutely WOW-worthy! This is perfect because:

- **Highly Practical**: Every professional needs to manage their network
- **Portfolio Gold**: Shows understanding of professional networking
- **Real-world Value**: Helps with job hunting, business development, career growth
- **TDD-Friendly**: Can build from basic contact management to sophisticated relationship tracking

## 🎯 **LinkedIn Networking Manager - 1 Week MVP Features**

### **Core Features:**
1. **Contact Management** - Add, categorize, and track LinkedIn connections
2. **Interaction History** - Log conversations, meetings, follow-ups
3. **Follow-up Reminders** - Never miss a follow-up opportunity
4. **Network Analytics** - Visualize your network strength and reach
5. **Connection Recommendations** - Suggest who to connect with next

### **TDD Progression:**
- **RED-001**: Basic LinkedIn contact creation and management
- **RED-002**: Interaction logging and history tracking
- **RED-003**: Follow-up reminder system
- **RED-004**: Network strength scoring and analytics
- **RED-005**: Connection recommendations and insights

## �� **Let's Start with RED-001**

Here's the first test that will guide the GREEN team:

```python:linkedin_network_test.py
import pytest
from datetime import datetime, timedelta
from linkedin_network import LinkedInContact, NetworkManager

class TestLinkedInContact:
    """Test the LinkedInContact class that represents a connection"""
    
    def test_create_linkedin_contact(self):
        """Test creating a new LinkedIn connection"""
        contact = LinkedInContact(
            name="Sarah Johnson",
            title="Senior Software Engineer",
            company="Google",
            connection_date="2024-01-15",
            industry="Technology"
        )
        
        assert contact.name == "Sarah Johnson"
        assert contact.title == "Senior Software Engineer"
        assert contact.company == "Google"
        assert contact.connection_date == "2024-01-15"
        assert contact.industry == "Technology"
        assert contact.connection_strength == 1  # Default strength
    
    def test_contact_string_representation(self):
        """Test that contacts display nicely"""
        contact = LinkedInContact(
            name="Mike Chen",
            title="Product Manager",
            company="Microsoft",
            connection_date="2024-01-20",
            industry="Technology"
        )
        
        expected = "Mike Chen - Product Manager at Microsoft (Connected: 2024-01-20)"
        assert str(contact) == expected
    
    def test_update_contact_info(self):
        """Test updating contact information"""
        contact = LinkedInContact(
            name="Alex Smith",
            title="Junior Developer",
            company="Startup Inc",
            connection_date="2024-01-10",
            industry="Technology"
        )
        
        # Update job info
        contact.update_info(
            title="Senior Developer",
            company="Big Tech Corp"
        )
        
        assert contact.title == "Senior Developer"
        assert contact.company == "Big Tech Corp"
        assert contact.name == "Alex Smith"  # Name shouldn't change

class TestNetworkManager:
    """Test the NetworkManager that handles multiple connections"""
    
    def test_add_contact(self):
        """Test adding a contact to the network"""
        manager = NetworkManager()
        contact = LinkedInContact(
            name="Jane Doe",
            title="Data Scientist",
            company="Netflix",
            connection_date="2024-01-25",
            industry="Entertainment"
        )
        
        manager.add_contact(contact)
        assert len(manager.contacts) == 1
        assert manager.contacts[0].name == "Jane Doe"
    
    def test_find_contacts_by_company(self):
        """Test finding contacts at specific companies"""
        manager = NetworkManager()
        
        # Add contacts from different companies
        google_contact = LinkedInContact("John", "Engineer", "Google", "2024-01-01", "Technology")
        microsoft_contact = LinkedInContact("Lisa", "Manager", "Microsoft", "2024-01-02", "Technology")
        google_contact2 = LinkedInContact("Tom", "Designer", "Google", "2024-01-03", "Technology")
        
        manager.add_contact(google_contact)
        manager.add_contact(microsoft_contact)
        manager.add_contact(google_contact2)
        
        google_contacts = manager.find_contacts_by_company("Google")
        assert len(google_contacts) == 2
        assert all(contact.company == "Google" for contact in google_contacts)
        
        microsoft_contacts = manager.find_contacts_by_company("Microsoft")
        assert len(microsoft_contacts) == 1
        assert microsoft_contacts[0].name == "Lisa"
    
    def test_get_contacts_by_industry(self):
        """Test filtering contacts by industry"""
        manager = NetworkManager()
        
        tech_contact = LinkedInContact("Alice", "Developer", "Tech Corp", "2024-01-01", "Technology")
        finance_contact = LinkedInContact("Bob", "Analyst", "Bank Inc", "2024-01-02", "Finance")
        tech_contact2 = LinkedInContact("Charlie", "PM", "Startup", "2024-01-03", "Technology")
        
        manager.add_contact(tech_contact)
        manager.add_contact(finance_contact)
        manager.add_contact(tech_contact2)
        
        tech_contacts = manager.get_contacts_by_industry("Technology")
        assert len(tech_contacts) == 2
        assert all(contact.industry == "Technology" for contact in tech_contacts)
        
        finance_contacts = manager.get_contacts_by_industry("Finance")
        assert len(finance_contacts) == 1
        assert finance_contacts[0].name == "Bob"
    
    def test_get_total_connections(self):
        """Test counting total connections"""
        manager = NetworkManager()
        
        manager.add_contact(LinkedInContact("Person 1", "Title 1", "Company 1", "2024-01-01", "Industry 1"))
        manager.add_contact(LinkedInContact("Person 2", "Title 2", "Company 2", "2024-01-02", "Industry 2"))
        manager.add_contact(LinkedInContact("Person 3", "Title 3", "Company 3", "2024-01-03", "Industry 3"))
        
        assert manager.get_total_connections() == 3
```

And here's the corresponding implementation file:

```python:linkedin_network.py
from datetime import datetime

class LinkedInContact:
    """Represents a LinkedIn connection"""
    
    def __init__(self, name, title, company, connection_date, industry, connection_strength=1):
        self.name = name
        self.title = title
        self.company = company
        self.connection_date = connection_date
        self.industry = industry
        self.connection_strength = connection_strength  # 1-5 scale
        self.interactions = []  # Will be used in future iterations
    
    def __str__(self):
        return f"{self.name} - {self.title} at {self.company} (Connected: {self.connection_date})"
    
    def update_info(self, title=None, company=None, industry=None):
        """Update contact information"""
        if title:
            self.title = title
        if company:
            self.company = company
        if industry:
            self.industry = industry

class NetworkManager:
    """Manages a collection of LinkedIn connections"""
    
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        """Add a contact to the network"""
        self.contacts.append(contact)
    
    def find_contacts_by_company(self, company):
        """Find all contacts at a specific company"""
        return [contact for contact in self.contacts if contact.company.lower() == company.lower()]
    
    def get_contacts_by_industry(self, industry):
        """Get all contacts in a specific industry"""
        return [contact for contact in self.contacts if contact.industry.lower() == industry.lower()]
    
    def get_total_connections(self):
        """Get the total number of connections"""
        return len(self.contacts)
```

## 🎯 **What This RED-001 Test Reveals:**

The GREEN team will discover they're building:
- A LinkedIn contact management system
- Contacts have name, title, company, connection date, industry
- They can filter contacts by company and industry
- They can count total connections

**But they won't know yet about:**
- Interaction tracking
- Follow-up reminders
- Network analytics
- Connection recommendations
- Relationship strength scoring

This creates the perfect foundation! Each subsequent RED branch will add more sophisticated networking features while keeping the GREEN team guessing about the final professional networking capabilities.

Would you like me to create the RED-002 test that would add interaction tracking functionality?

```python
import pytest
from datetime import datetime, timedelta
from linkedin_network import LinkedInContact, NetworkManager

class TestLinkedInContact:
    """Test the LinkedInContact class that represents a connection"""
    
    def test_create_linkedin_contact(self):
        """Test creating a new LinkedIn connection"""
        contact = LinkedInContact(
            name="Sarah Johnson",
            title="Senior Software Engineer",
            company="Google",
            connection_date="2024-01-15",
            industry="Technology"
        )
        
        assert contact.name == "Sarah Johnson"
        assert contact.title == "Senior Software Engineer"
        assert contact.company == "Google"
        assert contact.connection_date == "2024-01-15"
        assert contact.industry == "Technology"
        assert contact.connection_strength == 1  # Default strength
    
    def test_contact_string_representation(self):
        """Test that contacts display nicely"""
        contact = LinkedInContact(
            name="Mike Chen",
            title="Product Manager",
            company="Microsoft",
            connection_date="2024-01-20",
            industry="Technology"
        )
        
        expected = "Mike Chen - Product Manager at Microsoft (Connected: 2024-01-20)"
        assert str(contact) == expected
    
    def test_update_contact_info(self):
        """Test updating contact information"""
        contact = LinkedInContact(
            name="Alex Smith",
            title="Junior Developer",
            company="Startup Inc",
            connection_date="2024-01-10",
            industry="Technology"
        )
        
        # Update job info
        contact.update_info(
            title="Senior Developer",
            company="Big Tech Corp"
        )
        
        assert contact.title == "Senior Developer"
        assert contact.company == "Big Tech Corp"
        assert contact.name == "Alex Smith"  # Name shouldn't change

class TestNetworkManager:
    """Test the NetworkManager that handles multiple connections"""
    
    def test_add_contact(self):
        """Test adding a contact to the network"""
        manager = NetworkManager()
        contact = LinkedInContact(
            name="Jane Doe",
            title="Data Scientist",
            company="Netflix",
            connection_date="2024-01-25",
            industry="Entertainment"
        )
        
        manager.add_contact(contact)
        assert len(manager.contacts) == 1
        assert manager.contacts[0].name == "Jane Doe"
    
    def test_find_contacts_by_company(self):
        """Test finding contacts at specific companies"""
        manager = NetworkManager()
        
        # Add contacts from different companies
        google_contact = LinkedInContact("John", "Engineer", "Google", "2024-01-01", "Technology")
        microsoft_contact = LinkedInContact("Lisa", "Manager", "Microsoft", "2024-01-02", "Technology")
        google_contact2 = LinkedInContact("Tom", "Designer", "Google", "2024-01-03", "Technology")
        
        manager.add_contact(google_contact)
        manager.add_contact(microsoft_contact)
        manager.add_contact(google_contact2)
        
        google_contacts = manager.find_contacts_by_company("Google")
        assert len(google_contacts) == 2
        assert all(contact.company == "Google" for contact in google_contacts)
        
        microsoft_contacts = manager.find_contacts_by_company("Microsoft")
        assert len(microsoft_contacts) == 1
        assert microsoft_contacts[0].name == "Lisa"
    
    def test_get_contacts_by_industry(self):
        """Test filtering contacts by industry"""
        manager = NetworkManager()
        
        tech_contact = LinkedInContact("Alice", "Developer", "Tech Corp", "2024-01-01", "Technology")
        finance_contact = LinkedInContact("Bob", "Analyst", "Bank Inc", "2024-01-02", "Finance")
        tech_contact2 = LinkedInContact("Charlie", "PM", "Startup", "2024-01-03", "Technology")
        
        manager.add_contact(tech_contact)
        manager.add_contact(finance_contact)
        manager.add_contact(tech_contact2)
        
        tech_contacts = manager.get_contacts_by_industry("Technology")
        assert len(tech_contacts) == 2
        assert all(contact.industry == "Technology" for contact in tech_contacts)
        
        finance_contacts = manager.get_contacts_by_industry("Finance")
        assert len(finance_contacts) == 1
        assert finance_contacts[0].name == "Bob"
    
    def test_get_total_connections(self):
        """Test counting total connections"""
        manager = NetworkManager()
        
        manager.add_contact(LinkedInContact("Person 1", "Title 1", "Company 1", "2024-01-01", "Industry 1"))
        manager.add_contact(LinkedInContact("Person 2", "Title 2", "Company 2", "2024-01-02", "Industry 2"))
        manager.add_contact(LinkedInContact("Person 3", "Title 3", "Company 3", "2024-01-03", "Industry 3"))
        
        assert manager.get_total_connections() == 3
```

```python
from datetime import datetime

class LinkedInContact:
    """Represents a LinkedIn connection"""
    
    def __init__(self, name, title, company, connection_date, industry, connection_strength=1):
        self.name = name
        self.title = title
        self.company = company
        self.connection_date = connection_date
        self.industry = industry
        self.connection_strength = connection_strength  # 1-5 scale
        self.interactions = []  # Will be used in future iterations
    
    def __str__(self):
        return f"{self.name} - {self.title} at {self.company} (Connected: {self.connection_date})"
    
    def update_info(self, title=None, company=None, industry=None):
        """Update contact information"""
        if title:
            self.title = title
        if company:
            self.company = company
        if industry:
            self.industry = industry

class NetworkManager:
    """Manages a collection of LinkedIn connections"""
    
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, contact):
        """Add a contact to the network"""
        self.contacts.append(contact)
    
    def find_contacts_by_company(self, company):
        """Find all contacts at a specific company"""
        return [contact for contact in self.contacts if contact.company.lower() == company.lower()]
    
    def get_contacts_by_industry(self, industry):
        """Get all contacts in a specific industry"""
        return [contact for contact in self.contacts if contact.industry.lower() == industry.lower()]
    
    def get_total_connections(self):
        """Get the total number of connections"""
        return len(self.contacts)
```

---

**User**

show how you expect the reminders to work, both tests and code

---

**Cursor**

Excellent! Let me show you how the **RED-003** follow-up reminder system would work. This is where the networking manager gets really powerful!

## 🎯 **RED-003: Follow-up Reminder System**

Here's the test that would guide the GREEN team to build the reminder functionality:

```python:linkedin_network_test.py
import pytest
from datetime import datetime, timedelta
from linkedin_network import LinkedInContact, NetworkManager, Interaction, ReminderSystem

class TestInteraction:
    """Test the Interaction class that tracks conversations and meetings"""
    
    def test_create_interaction(self):
        """Test creating a new interaction with a contact"""
        interaction = Interaction(
            contact_name="Sarah Johnson",
            interaction_type="Coffee Meeting",
            date="2024-01-15",
            notes="Discussed potential collaboration on AI project",
            follow_up_needed=True
        )
        
        assert interaction.contact_name == "Sarah Johnson"
        assert interaction.interaction_type == "Coffee Meeting"
        assert interaction.date == "2024-01-15"
        assert interaction.notes == "Discussed potential collaboration on AI project"
        assert interaction.follow_up_needed == True
        assert interaction.completed == False
    
    def test_interaction_string_representation(self):
        """Test that interactions display nicely"""
        interaction = Interaction(
            contact_name="Mike Chen",
            interaction_type="LinkedIn Message",
            date="2024-01-20",
            notes="Congratulated on new role",
            follow_up_needed=False
        )
        
        expected = "LinkedIn Message with Mike Chen on 2024-01-20"
        assert str(interaction) == expected

class TestReminderSystem:
    """Test the reminder system for follow-ups"""
    
    def test_create_follow_up_reminder(self):
        """Test creating a reminder for a follow-up"""
        reminder = ReminderSystem()
        
        reminder.create_reminder(
            contact_name="Jane Doe",
            due_date="2024-01-25",
            action="Send follow-up email about project proposal",
            priority="High"
        )
        
        reminders = reminder.get_pending_reminders()
        assert len(reminders) == 1
        assert reminders[0]["contact_name"] == "Jane Doe"
        assert reminders[0]["action"] == "Send follow-up email about project proposal"
        assert reminders[0]["priority"] == "High"
    
    def test_get_overdue_reminders(self):
        """Test finding reminders that are past due"""
        reminder = ReminderSystem()
        
        # Create a reminder that's overdue (yesterday)
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        reminder.create_reminder(
            contact_name="Overdue Contact",
            due_date=yesterday,
            action="Send thank you note",
            priority="Medium"
        )
        
        # Create a reminder that's due today
        today = datetime.now().strftime("%Y-%m-%d")
        reminder.create_reminder(
            contact_name="Today Contact",
            due_date=today,
            action="Schedule coffee meeting",
            priority="High"
        )
        
        overdue = reminder.get_overdue_reminders()
        assert len(overdue) == 1
        assert overdue[0]["contact_name"] == "Overdue Contact"
    
    def test_mark_reminder_completed(self):
        """Test marking a reminder as completed"""
        reminder = ReminderSystem()
        
        reminder.create_reminder(
            contact_name="Test Contact",
            due_date="2024-01-30",
            action="Send LinkedIn message",
            priority="Low"
        )
        
        # Mark as completed
        reminder.mark_completed("Test Contact", "Send LinkedIn message")
        
        pending = reminder.get_pending_reminders()
        assert len(pending) == 0
        
        completed = reminder.get_completed_reminders()
        assert len(completed) == 1
        assert completed[0]["contact_name"] == "Test Contact"
    
    def test_get_reminders_by_priority(self):
        """Test filtering reminders by priority"""
        reminder = ReminderSystem()
        
        reminder.create_reminder("Contact A", "2024-01-25", "Urgent call", "High")
        reminder.create_reminder("Contact B", "2024-01-26", "Send article", "Medium")
        reminder.create_reminder("Contact C", "2024-01-27", "Connect on LinkedIn", "Low")
        reminder.create_reminder("Contact D", "2024-01-28", "Follow up on job", "High")
        
        high_priority = reminder.get_reminders_by_priority("High")
        assert len(high_priority) == 2
        assert all(r["priority"] == "High" for r in high_priority)
        
        low_priority = reminder.get_reminders_by_priority("Low")
        assert len(low_priority) == 1
        assert low_priority[0]["contact_name"] == "Contact C"

class TestNetworkManagerWithReminders:
    """Test how NetworkManager integrates with the reminder system"""
    
    def test_add_interaction_with_reminder(self):
        """Test adding an interaction that creates a follow-up reminder"""
        manager = NetworkManager()
        reminder_system = ReminderSystem()
        
        # Add a contact
        contact = LinkedInContact("Alex Smith", "PM", "Tech Corp", "2024-01-10", "Technology")
        manager.add_contact(contact)
        
        # Add an interaction that needs follow-up
        interaction = Interaction(
            contact_name="Alex Smith",
            interaction_type="Phone Call",
            date="2024-01-15",
            notes="Discussed job opportunity, needs follow-up in 1 week",
            follow_up_needed=True
        )
        
        manager.add_interaction(interaction)
        
        # Create reminder for follow-up
        follow_up_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        reminder_system.create_reminder(
            contact_name="Alex Smith",
            due_date=follow_up_date,
            action="Follow up on job opportunity discussed in phone call",
            priority="High"
        )
        
        # Verify interaction was logged
        interactions = manager.get_interactions_for_contact("Alex Smith")
        assert len(interactions) == 1
        assert interactions[0].interaction_type == "Phone Call"
        
        # Verify reminder was created
        reminders = reminder_system.get_pending_reminders()
        assert len(reminders) == 1
        assert reminders[0]["contact_name"] == "Alex Smith"
    
    def test_get_contacts_needing_follow_up(self):
        """Test finding contacts who need follow-up"""
        manager = NetworkManager()
        reminder_system = ReminderSystem()
        
        # Add contacts with different follow-up needs
        contact1 = LinkedInContact("Person A", "Title A", "Company A", "2024-01-01", "Industry A")
        contact2 = LinkedInContact("Person B", "Title B", "Company B", "2024-01-02", "Industry B")
        contact3 = LinkedInContact("Person C", "Title C", "Company C", "2024-01-03", "Industry C")
        
        manager.add_contact(contact1)
        manager.add_contact(contact2)
        manager.add_contact(contact3)
        
        # Add interactions with follow-ups
        interaction1 = Interaction("Person A", "Meeting", "2024-01-15", "Great conversation", True)
        interaction2 = Interaction("Person B", "Message", "2024-01-16", "Quick chat", False)
        interaction3 = Interaction("Person C", "Call", "2024-01-17", "Job discussion", True)
        
        manager.add_interaction(interaction1)
        manager.add_interaction(interaction2)
        manager.add_interaction(interaction3)
        
        # Create reminders for follow-ups
        reminder_system.create_reminder("Person A", "2024-01-25", "Follow up on meeting", "Medium")
        reminder_system.create_reminder("Person C", "2024-01-26", "Send job application", "High")
        
        # Get contacts needing follow-up
        contacts_needing_follow_up = manager.get_contacts_needing_follow_up(reminder_system)
        assert len(contacts_needing_follow_up) == 2
        assert "Person A" in [c.name for c in contacts_needing_follow_up]
        assert "Person C" in [c.name for c in contacts_needing_follow_up]
        assert "Person B" not in [c.name for c in contacts_needing_follow_up]
```

And here's the corresponding implementation:

```python:linkedin_network.py
from datetime import datetime, timedelta

class LinkedInContact:
    """Represents a LinkedIn connection"""
    
    def __init__(self, name, title, company, connection_date, industry, connection_strength=1):
        self.name = name
        self.title = title
        self.company = company
        self.connection_date = connection_date
        self.industry = industry
        self.connection_strength = connection_strength
        self.interactions = []
    
    def __str__(self):
        return f"{self.name} - {self.title} at {self.company} (Connected: {self.connection_date})"
    
    def update_info(self, title=None, company=None, industry=None):
        if title:
            self.title = title
        if company:
            self.company = company
        if industry:
            self.industry = industry

class Interaction:
    """Represents an interaction with a contact"""
    
    def __init__(self, contact_name, interaction_type, date, notes, follow_up_needed=False):
        self.contact_name = contact_name
        self.interaction_type = interaction_type
        self.date = date
        self.notes = notes
        self.follow_up_needed = follow_up_needed
        self.completed = False
    
    def __str__(self):
        return f"{self.interaction_type} with {self.contact_name} on {self.date}"

class ReminderSystem:
    """Manages follow-up reminders for contacts"""
    
    def __init__(self):
        self.reminders = []
    
    def create_reminder(self, contact_name, due_date, action, priority="Medium"):
        """Create a new follow-up reminder"""
        reminder = {
            "contact_name": contact_name,
            "due_date": due_date,
            "action": action,
            "priority": priority,
            "completed": False,
            "created_date": datetime.now().strftime("%Y-%m-%d")
        }
        self.reminders.append(reminder)
    
    def get_pending_reminders(self):
        """Get all pending (incomplete) reminders"""
        return [r for r in self.reminders if not r["completed"]]
    
    def get_completed_reminders(self):
        """Get all completed reminders"""
        return [r for r in self.reminders if r["completed"]]
    
    def get_overdue_reminders(self):
        """Get reminders that are past due"""
        today = datetime.now().strftime("%Y-%m-%d")
        return [r for r in self.reminders 
                if not r["completed"] and r["due_date"] < today]
    
    def mark_completed(self, contact_name, action):
        """Mark a specific reminder as completed"""
        for reminder in self.reminders:
            if (reminder["contact_name"] == contact_name and 
                reminder["action"] == action and 
                not reminder["completed"]):
                reminder["completed"] = True
                break
    
    def get_reminders_by_priority(self, priority):
        """Get reminders filtered by priority"""
        return [r for r in self.reminders 
                if r["priority"] == priority and not r["completed"]]

class NetworkManager:
    """Manages a collection of LinkedIn connections with interactions and reminders"""
    
    def __init__(self):
        self.contacts = []
        self.interactions = []
    
    def add_contact(self, contact):
        """Add a contact to the network"""
        self.contacts.append(contact)
    
    def add_interaction(self, interaction):
        """Add an interaction with a contact"""
        self.interactions.append(interaction)
        
        # Add to contact's interaction list
        for contact in self.contacts:
            if contact.name == interaction.contact_name:
                contact.interactions.append(interaction)
                break
    
    def get_interactions_for_contact(self, contact_name):
        """Get all interactions for a specific contact"""
        return [i for i in self.interactions if i.contact_name == contact_name]
    
    def get_contacts_needing_follow_up(self, reminder_system):
        """Get contacts who have pending follow-up reminders"""
        pending_reminders = reminder_system.get_pending_reminders()
        contact_names = [r["contact_name"] for r in pending_reminders]
        
        return [contact for contact in self.contacts if contact.name in contact_names]
    
    def find_contacts_by_company(self, company):
        return [contact for contact in self.contacts if contact.company.lower() == company.lower()]
    
    def get_contacts_by_industry(self, industry):
        return [contact for contact in self.contacts if contact.industry.lower() == industry.lower()]
    
    def get_total_connections(self):
        return len(self.contacts)
```

## �� **How the Reminder System Works:**

### **Key Features:**
1. **Interaction Tracking**: Log every conversation, meeting, or message
2. **Follow-up Flags**: Mark interactions that need follow-up
3. **Priority System**: High, Medium, Low priority reminders
4. **Due Date Management**: Set specific dates for follow-ups
5. **Overdue Detection**: Find reminders that are past due
6. **Completion Tracking**: Mark reminders as done

### **Real-World Usage:**
```python
# Example workflow
manager = NetworkManager()
reminder_system = ReminderSystem()

# Add a contact
contact = LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology")
manager.add_contact(contact)

# Log an interaction that needs follow-up
interaction = Interaction(
    contact_name="Sarah Johnson",
    interaction_type="Coffee Meeting",
    date="2024-01-15",
    notes="Discussed potential job opportunity, she wants to see my portfolio",
    follow_up_needed=True
)
manager.add_interaction(interaction)

# Create a reminder
reminder_system.create_reminder(
    contact_name="Sarah Johnson",
    due_date="2024-01-22",  # 1 week later
    action="Send portfolio and follow up on job opportunity",
    priority="High"
)

# Later, check what needs attention
overdue = reminder_system.get_overdue_reminders()
high_priority = reminder_system.get_reminders_by_priority("High")
contacts_needing_follow_up = manager.get_contacts_needing_follow_up(reminder_system)
```

This creates a powerful system that helps professionals never miss important follow-ups and maintain strong relationships!

```python
import pytest
from datetime import datetime, timedelta
from linkedin_network import LinkedInContact, NetworkManager, Interaction, ReminderSystem

class TestInteraction:
    """Test the Interaction class that tracks conversations and meetings"""
    
    def test_create_interaction(self):
        """Test creating a new interaction with a contact"""
        interaction = Interaction(
            contact_name="Sarah Johnson",
            interaction_type="Coffee Meeting",
            date="2024-01-15",
            notes="Discussed potential collaboration on AI project",
            follow_up_needed=True
        )
        
        assert interaction.contact_name == "Sarah Johnson"
        assert interaction.interaction_type == "Coffee Meeting"
        assert interaction.date == "2024-01-15"
        assert interaction.notes == "Discussed potential collaboration on AI project"
        assert interaction.follow_up_needed == True
        assert interaction.completed == False
    
    def test_interaction_string_representation(self):
        """Test that interactions display nicely"""
        interaction = Interaction(
            contact_name="Mike Chen",
            interaction_type="LinkedIn Message",
            date="2024-01-20",
            notes="Congratulated on new role",
            follow_up_needed=False
        )
        
        expected = "LinkedIn Message with Mike Chen on 2024-01-20"
        assert str(interaction) == expected

class TestReminderSystem:
    """Test the reminder system for follow-ups"""
    
    def test_create_follow_up_reminder(self):
        """Test creating a reminder for a follow-up"""
        reminder = ReminderSystem()
        
        reminder.create_reminder(
            contact_name="Jane Doe",
            due_date="2024-01-25",
            action="Send follow-up email about project proposal",
            priority="High"
        )
        
        reminders = reminder.get_pending_reminders()
        assert len(reminders) == 1
        assert reminders[0]["contact_name"] == "Jane Doe"
        assert reminders[0]["action"] == "Send follow-up email about project proposal"
        assert reminders[0]["priority"] == "High"
    
    def test_get_overdue_reminders(self):
        """Test finding reminders that are past due"""
        reminder = ReminderSystem()
        
        # Create a reminder that's overdue (yesterday)
        yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        reminder.create_reminder(
            contact_name="Overdue Contact",
            due_date=yesterday,
            action="Send thank you note",
            priority="Medium"
        )
        
        # Create a reminder that's due today
        today = datetime.now().strftime("%Y-%m-%d")
        reminder.create_reminder(
            contact_name="Today Contact",
            due_date=today,
            action="Schedule coffee meeting",
            priority="High"
        )
        
        overdue = reminder.get_overdue_reminders()
        assert len(overdue) == 1
        assert overdue[0]["contact_name"] == "Overdue Contact"
    
    def test_mark_reminder_completed(self):
        """Test marking a reminder as completed"""
        reminder = ReminderSystem()
        
        reminder.create_reminder(
            contact_name="Test Contact",
            due_date="2024-01-30",
            action="Send LinkedIn message",
            priority="Low"
        )
        
        # Mark as completed
        reminder.mark_completed("Test Contact", "Send LinkedIn message")
        
        pending = reminder.get_pending_reminders()
        assert len(pending) == 0
        
        completed = reminder.get_completed_reminders()
        assert len(completed) == 1
        assert completed[0]["contact_name"] == "Test Contact"
    
    def test_get_reminders_by_priority(self):
        """Test filtering reminders by priority"""
        reminder = ReminderSystem()
        
        reminder.create_reminder("Contact A", "2024-01-25", "Urgent call", "High")
        reminder.create_reminder("Contact B", "2024-01-26", "Send article", "Medium")
        reminder.create_reminder("Contact C", "2024-01-27", "Connect on LinkedIn", "Low")
        reminder.create_reminder("Contact D", "2024-01-28", "Follow up on job", "High")
        
        high_priority = reminder.get_reminders_by_priority("High")
        assert len(high_priority) == 2
        assert all(r["priority"] == "High" for r in high_priority)
        
        low_priority = reminder.get_reminders_by_priority("Low")
        assert len(low_priority) == 1
        assert low_priority[0]["contact_name"] == "Contact C"

class TestNetworkManagerWithReminders:
    """Test how NetworkManager integrates with the reminder system"""
    
    def test_add_interaction_with_reminder(self):
        """Test adding an interaction that creates a follow-up reminder"""
        manager = NetworkManager()
        reminder_system = ReminderSystem()
        
        # Add a contact
        contact = LinkedInContact("Alex Smith", "PM", "Tech Corp", "2024-01-10", "Technology")
        manager.add_contact(contact)
        
        # Add an interaction that needs follow-up
        interaction = Interaction(
            contact_name="Alex Smith",
            interaction_type="Phone Call",
            date="2024-01-15",
            notes="Discussed job opportunity, needs follow-up in 1 week",
            follow_up_needed=True
        )
        
        manager.add_interaction(interaction)
        
        # Create reminder for follow-up
        follow_up_date = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")
        reminder_system.create_reminder(
            contact_name="Alex Smith",
            due_date=follow_up_date,
            action="Follow up on job opportunity discussed in phone call",
            priority="High"
        )
        
        # Verify interaction was logged
        interactions = manager.get_interactions_for_contact("Alex Smith")
        assert len(interactions) == 1
        assert interactions[0].interaction_type == "Phone Call"
        
        # Verify reminder was created
        reminders = reminder_system.get_pending_reminders()
        assert len(reminders) == 1
        assert reminders[0]["contact_name"] == "Alex Smith"
    
    def test_get_contacts_needing_follow_up(self):
        """Test finding contacts who need follow-up"""
        manager = NetworkManager()
        reminder_system = ReminderSystem()
        
        # Add contacts with different follow-up needs
        contact1 = LinkedInContact("Person A", "Title A", "Company A", "2024-01-01", "Industry A")
        contact2 = LinkedInContact("Person B", "Title B", "Company B", "2024-01-02", "Industry B")
        contact3 = LinkedInContact("Person C", "Title C", "Company C", "2024-01-03", "Industry C")
        
        manager.add_contact(contact1)
        manager.add_contact(contact2)
        manager.add_contact(contact3)
        
        # Add interactions with follow-ups
        interaction1 = Interaction("Person A", "Meeting", "2024-01-15", "Great conversation", True)
        interaction2 = Interaction("Person B", "Message", "2024-01-16", "Quick chat", False)
        interaction3 = Interaction("Person C", "Call", "2024-01-17", "Job discussion", True)
        
        manager.add_interaction(interaction1)
        manager.add_interaction(interaction2)
        manager.add_interaction(interaction3)
        
        # Create reminders for follow-ups
        reminder_system.create_reminder("Person A", "2024-01-25", "Follow up on meeting", "Medium")
        reminder_system.create_reminder("Person C", "2024-01-26", "Send job application", "High")
        
        # Get contacts needing follow-up
        contacts_needing_follow_up = manager.get_contacts_needing_follow_up(reminder_system)
        assert len(contacts_needing_follow_up) == 2
        assert "Person A" in [c.name for c in contacts_needing_follow_up]
        assert "Person C" in [c.name for c in contacts_needing_follow_up]
        assert "Person B" not in [c.name for c in contacts_needing_follow_up]
```

```python
from datetime import datetime, timedelta

class LinkedInContact:
    """Represents a LinkedIn connection"""
    
    def __init__(self, name, title, company, connection_date, industry, connection_strength=1):
        self.name = name
        self.title = title
        self.company = company
        self.connection_date = connection_date
        self.industry = industry
        self.connection_strength = connection_strength
        self.interactions = []
    
    def __str__(self):
        return f"{self.name} - {self.title} at {self.company} (Connected: {self.connection_date})"
    
    def update_info(self, title=None, company=None, industry=None):
        if title:
            self.title = title
        if company:
            self.company = company
        if industry:
            self.industry = industry

class Interaction:
    """Represents an interaction with a contact"""
    
    def __init__(self, contact_name, interaction_type, date, notes, follow_up_needed=False):
        self.contact_name = contact_name
        self.interaction_type = interaction_type
        self.date = date
        self.notes = notes
        self.follow_up_needed = follow_up_needed
        self.completed = False
    
    def __str__(self):
        return f"{self.interaction_type} with {self.contact_name} on {self.date}"

class ReminderSystem:
    """Manages follow-up reminders for contacts"""
    
    def __init__(self):
        self.reminders = []
    
    def create_reminder(self, contact_name, due_date, action, priority="Medium"):
        """Create a new follow-up reminder"""
        reminder = {
            "contact_name": contact_name,
            "due_date": due_date,
            "action": action,
            "priority": priority,
            "completed": False,
            "created_date": datetime.now().strftime("%Y-%m-%d")
        }
        self.reminders.append(reminder)
    
    def get_pending_reminders(self):
        """Get all pending (incomplete) reminders"""
        return [r for r in self.reminders if not r["completed"]]
    
    def get_completed_reminders(self):
        """Get all completed reminders"""
        return [r for r in self.reminders if r["completed"]]
    
    def get_overdue_reminders(self):
        """Get reminders that are past due"""
        today = datetime.now().strftime("%Y-%m-%d")
        return [r for r in self.reminders 
                if not r["completed"] and r["due_date"] < today]
    
    def mark_completed(self, contact_name, action):
        """Mark a specific reminder as completed"""
        for reminder in self.reminders:
            if (reminder["contact_name"] == contact_name and 
                reminder["action"] == action and 
                not reminder["completed"]):
                reminder["completed"] = True
                break
    
    def get_reminders_by_priority(self, priority):
        """Get reminders filtered by priority"""
        return [r for r in self.reminders 
                if r["priority"] == priority and not r["completed"]]

class NetworkManager:
    """Manages a collection of LinkedIn connections with interactions and reminders"""
    
    def __init__(self):
        self.contacts = []
        self.interactions = []
    
    def add_contact(self, contact):
        """Add a contact to the network"""
        self.contacts.append(contact)
    
    def add_interaction(self, interaction):
        """Add an interaction with a contact"""
        self.interactions.append(interaction)
        
        # Add to contact's interaction list
        for contact in self.contacts:
            if contact.name == interaction.contact_name:
                contact.interactions.append(interaction)
                break
    
    def get_interactions_for_contact(self, contact_name):
        """Get all interactions for a specific contact"""
        return [i for i in self.interactions if i.contact_name == contact_name]
    
    def get_contacts_needing_follow_up(self, reminder_system):
        """Get contacts who have pending follow-up reminders"""
        pending_reminders = reminder_system.get_pending_reminders()
        contact_names = [r["contact_name"] for r in pending_reminders]
        
        return [contact for contact in self.contacts if contact.name in contact_names]
    
    def find_contacts_by_company(self, company):
        return [contact for contact in self.contacts if contact.company.lower() == company.lower()]
    
    def get_contacts_by_industry(self, industry):
        return [contact for contact in self.contacts if contact.industry.lower() == industry.lower()]
    
    def get_total_connections(self):
        return len(self.contacts)
```

```python
# Example workflow
manager = NetworkManager()
reminder_system = ReminderSystem()

# Add a contact
contact = LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology")
manager.add_contact(contact)

# Log an interaction that needs follow-up
interaction = Interaction(
    contact_name="Sarah Johnson",
    interaction_type="Coffee Meeting",
    date="2024-01-15",
    notes="Discussed potential job opportunity, she wants to see my portfolio",
    follow_up_needed=True
)
manager.add_interaction(interaction)

# Create a reminder
reminder_system.create_reminder(
    contact_name="Sarah Johnson",
    due_date="2024-01-22",  # 1 week later
    action="Send portfolio and follow up on job opportunity",
    priority="High"
)

# Later, check what needs attention
overdue = reminder_system.get_overdue_reminders()
high_priority = reminder_system.get_reminders_by_priority("High")
contacts_needing_follow_up = manager.get_contacts_needing_follow_up(reminder_system)
```

---

**User**

show how to use google sheets and a csv to store the data in a way that can be pulled for this

---

**Cursor**

Excellent idea! Let me show you how to integrate Google Sheets and CSV storage for the LinkedIn Networking Manager. This makes it much more practical and accessible!

## 🎯 **RED-004: Data Persistence with Google Sheets & CSV**

Here's the test that would guide the GREEN team to build data storage:

```python:linkedin_network_test.py
import pytest
import pandas as pd
from unittest.mock import Mock, patch
from linkedin_network import (
    LinkedInContact, NetworkManager, Interaction, ReminderSystem,
    CSVDataManager, GoogleSheetsManager
)

class TestCSVDataManager:
    """Test CSV-based data storage and retrieval"""
    
    def test_save_contacts_to_csv(self, tmp_path):
        """Test saving contacts to a CSV file"""
        data_manager = CSVDataManager()
        manager = NetworkManager()
        
        # Add some contacts
        contact1 = LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology")
        contact2 = LinkedInContact("Mike Chen", "Product Manager", "Microsoft", "2024-01-15", "Technology")
        manager.add_contact(contact1)
        manager.add_contact(contact2)
        
        # Save to CSV
        csv_file = tmp_path / "contacts.csv"
        data_manager.save_contacts(manager.contacts, str(csv_file))
        
        # Verify file was created and contains data
        assert csv_file.exists()
        df = pd.read_csv(csv_file)
        assert len(df) == 2
        assert "Sarah Johnson" in df["name"].values
        assert "Mike Chen" in df["name"].values
    
    def test_load_contacts_from_csv(self, tmp_path):
        """Test loading contacts from a CSV file"""
        data_manager = CSVDataManager()
        
        # Create a test CSV file
        csv_file = tmp_path / "test_contacts.csv"
        test_data = {
            "name": ["Alice Smith", "Bob Johnson"],
            "title": ["Data Scientist", "Software Engineer"],
            "company": ["Netflix", "Amazon"],
            "connection_date": ["2024-01-01", "2024-01-02"],
            "industry": ["Entertainment", "Technology"],
            "connection_strength": [3, 4]
        }
        df = pd.DataFrame(test_data)
        df.to_csv(csv_file, index=False)
        
        # Load contacts
        contacts = data_manager.load_contacts(str(csv_file))
        
        assert len(contacts) == 2
        assert contacts[0].name == "Alice Smith"
        assert contacts[0].title == "Data Scientist"
        assert contacts[1].name == "Bob Johnson"
        assert contacts[1].company == "Amazon"
    
    def test_save_interactions_to_csv(self, tmp_path):
        """Test saving interactions to a CSV file"""
        data_manager = CSVDataManager()
        interactions = [
            Interaction("Sarah Johnson", "Coffee Meeting", "2024-01-15", "Great conversation", True),
            Interaction("Mike Chen", "LinkedIn Message", "2024-01-16", "Quick chat", False)
        ]
        
        csv_file = tmp_path / "interactions.csv"
        data_manager.save_interactions(interactions, str(csv_file))
        
        assert csv_file.exists()
        df = pd.read_csv(csv_file)
        assert len(df) == 2
        assert "Coffee Meeting" in df["interaction_type"].values
        assert "LinkedIn Message" in df["interaction_type"].values
    
    def test_save_reminders_to_csv(self, tmp_path):
        """Test saving reminders to a CSV file"""
        data_manager = CSVDataManager()
        reminder_system = ReminderSystem()
        
        reminder_system.create_reminder("Sarah Johnson", "2024-01-25", "Follow up on meeting", "High")
        reminder_system.create_reminder("Mike Chen", "2024-01-26", "Send thank you note", "Medium")
        
        csv_file = tmp_path / "reminders.csv"
        data_manager.save_reminders(reminder_system.reminders, str(csv_file))
        
        assert csv_file.exists()
        df = pd.read_csv(csv_file)
        assert len(df) == 2
        assert "Sarah Johnson" in df["contact_name"].values
        assert "High" in df["priority"].values

class TestGoogleSheetsManager:
    """Test Google Sheets integration for data storage"""
    
    @patch('gspread.authorize')
    def test_connect_to_google_sheets(self, mock_authorize):
        """Test connecting to Google Sheets"""
        sheets_manager = GoogleSheetsManager()
        
        # Mock the Google Sheets connection
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        sheets_manager.connect("path/to/credentials.json")
        
        assert sheets_manager.client is not None
        mock_authorize.assert_called_once()
    
    @patch('gspread.authorize')
    def test_create_or_open_spreadsheet(self, mock_authorize):
        """Test creating or opening a spreadsheet"""
        sheets_manager = GoogleSheetsManager()
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        # Mock spreadsheet operations
        mock_spreadsheet = Mock()
        mock_client.open.return_value = mock_spreadsheet
        mock_client.create.return_value = mock_spreadsheet
        
        sheets_manager.connect("path/to/credentials.json")
        
        # Test opening existing spreadsheet
        spreadsheet = sheets_manager.create_or_open_spreadsheet("LinkedIn Network")
        assert spreadsheet is not None
        
        # Test creating new spreadsheet
        mock_client.open.side_effect = Exception("Not found")
        spreadsheet = sheets_manager.create_or_open_spreadsheet("New Network")
        assert spreadsheet is not None
    
    @patch('gspread.authorize')
    def test_save_contacts_to_sheets(self, mock_authorize):
        """Test saving contacts to Google Sheets"""
        sheets_manager = GoogleSheetsManager()
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        mock_spreadsheet = Mock()
        mock_worksheet = Mock()
        mock_spreadsheet.worksheet.return_value = mock_worksheet
        mock_client.open.return_value = mock_spreadsheet
        
        sheets_manager.connect("path/to/credentials.json")
        spreadsheet = sheets_manager.create_or_open_spreadsheet("Test Network")
        
        # Create test contacts
        contacts = [
            LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology"),
            LinkedInContact("Mike Chen", "Product Manager", "Microsoft", "2024-01-15", "Technology")
        ]
        
        # Save contacts
        sheets_manager.save_contacts_to_sheet(spreadsheet, contacts)
        
        # Verify worksheet was accessed and data was updated
        mock_spreadsheet.worksheet.assert_called_with("Contacts")
        mock_worksheet.clear.assert_called_once()
        mock_worksheet.update.assert_called_once()
    
    @patch('gspread.authorize')
    def test_load_contacts_from_sheets(self, mock_authorize):
        """Test loading contacts from Google Sheets"""
        sheets_manager = GoogleSheetsManager()
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        mock_spreadsheet = Mock()
        mock_worksheet = Mock()
        mock_spreadsheet.worksheet.return_value = mock_worksheet
        mock_client.open.return_value = mock_spreadsheet
        
        # Mock worksheet data
        mock_worksheet.get_all_records.return_value = [
            {
                "name": "Sarah Johnson",
                "title": "Engineering Manager",
                "company": "Google",
                "connection_date": "2024-01-10",
                "industry": "Technology",
                "connection_strength": 3
            },
            {
                "name": "Mike Chen",
                "title": "Product Manager",
                "company": "Microsoft",
                "connection_date": "2024-01-15",
                "industry": "Technology",
                "connection_strength": 4
            }
        ]
        
        sheets_manager.connect("path/to/credentials.json")
        spreadsheet = sheets_manager.create_or_open_spreadsheet("Test Network")
        
        # Load contacts
        contacts = sheets_manager.load_contacts_from_sheet(spreadsheet)
        
        assert len(contacts) == 2
        assert contacts[0].name == "Sarah Johnson"
        assert contacts[1].name == "Mike Chen"

class TestDataSync:
    """Test syncing data between different storage methods"""
    
    def test_sync_csv_to_sheets(self, tmp_path):
        """Test syncing data from CSV to Google Sheets"""
        # Create test CSV
        csv_file = tmp_path / "contacts.csv"
        test_data = {
            "name": ["Alice Smith", "Bob Johnson"],
            "title": ["Data Scientist", "Software Engineer"],
            "company": ["Netflix", "Amazon"],
            "connection_date": ["2024-01-01", "2024-01-02"],
            "industry": ["Entertainment", "Technology"],
            "connection_strength": [3, 4]
        }
        df = pd.DataFrame(test_data)
        df.to_csv(csv_file, index=False)
        
        # Load from CSV
        csv_manager = CSVDataManager()
        contacts = csv_manager.load_contacts(str(csv_file))
        
        # Mock Google Sheets sync
        with patch('gspread.authorize') as mock_authorize:
            sheets_manager = GoogleSheetsManager()
            mock_client = Mock()
            mock_authorize.return_value = mock_client
            
            mock_spreadsheet = Mock()
            mock_worksheet = Mock()
            mock_spreadsheet.worksheet.return_value = mock_worksheet
            mock_client.open.return_value = mock_spreadsheet
            
            sheets_manager.connect("path/to/credentials.json")
            spreadsheet = sheets_manager.create_or_open_spreadsheet("Synced Network")
            
            # Sync to sheets
            sheets_manager.save_contacts_to_sheet(spreadsheet, contacts)
            
            # Verify sync happened
            mock_worksheet.clear.assert_called_once()
            mock_worksheet.update.assert_called_once()
```

And here's the implementation:

```python:linkedin_network.py
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os

class CSVDataManager:
    """Manages data storage and retrieval using CSV files"""
    
    def save_contacts(self, contacts, filepath):
        """Save contacts to a CSV file"""
        data = []
        for contact in contacts:
            data.append({
                "name": contact.name,
                "title": contact.title,
                "company": contact.company,
                "connection_date": contact.connection_date,
                "industry": contact.industry,
                "connection_strength": contact.connection_strength
            })
        
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
    
    def load_contacts(self, filepath):
        """Load contacts from a CSV file"""
        if not os.path.exists(filepath):
            return []
        
        df = pd.read_csv(filepath)
        contacts = []
        
        for _, row in df.iterrows():
            contact = LinkedInContact(
                name=row["name"],
                title=row["title"],
                company=row["company"],
                connection_date=row["connection_date"],
                industry=row["industry"],
                connection_strength=row["connection_strength"]
            )
            contacts.append(contact)
        
        return contacts
    
    def save_interactions(self, interactions, filepath):
        """Save interactions to a CSV file"""
        data = []
        for interaction in interactions:
            data.append({
                "contact_name": interaction.contact_name,
                "interaction_type": interaction.interaction_type,
                "date": interaction.date,
                "notes": interaction.notes,
                "follow_up_needed": interaction.follow_up_needed,
                "completed": interaction.completed
            })
        
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
    
    def save_reminders(self, reminders, filepath):
        """Save reminders to a CSV file"""
        df = pd.DataFrame(reminders)
        df.to_csv(filepath, index=False)

class GoogleSheetsManager:
    """Manages data storage and retrieval using Google Sheets"""
    
    def __init__(self):
        self.client = None
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
    
    def connect(self, credentials_path):
        """Connect to Google Sheets API"""
        credentials = Credentials.from_service_account_file(
            credentials_path, scopes=self.scope
        )
        self.client = gspread.authorize(credentials)
    
    def create_or_open_spreadsheet(self, title):
        """Create a new spreadsheet or open existing one"""
        try:
            spreadsheet = self.client.open(title)
        except gspread.SpreadsheetNotFound:
            spreadsheet = self.client.create(title)
        return spreadsheet
    
    def save_contacts_to_sheet(self, spreadsheet, contacts):
        """Save contacts to a Google Sheet"""
        worksheet = spreadsheet.worksheet("Contacts")
        worksheet.clear()
        
        # Prepare headers
        headers = ["name", "title", "company", "connection_date", "industry", "connection_strength"]
        worksheet.append_row(headers)
        
        # Prepare data
        data = []
        for contact in contacts:
            data.append([
                contact.name,
                contact.title,
                contact.company,
                contact.connection_date,
                contact.industry,
                contact.connection_strength
            ])
        
        if data:
            worksheet.append_rows(data)
    
    def load_contacts_from_sheet(self, spreadsheet):
        """Load contacts from a Google Sheet"""
        try:
            worksheet = spreadsheet.worksheet("Contacts")
            records = worksheet.get_all_records()
            
            contacts = []
            for record in records:
                contact = LinkedInContact(
                    name=record["name"],
                    title=record["title"],
                    company=record["company"],
                    connection_date=record["connection_date"],
                    industry=record["industry"],
                    connection_strength=record["connection_strength"]
                )
                contacts.append(contact)
            
            return contacts
        except gspread.WorksheetNotFound:
            return []
    
    def save_interactions_to_sheet(self, spreadsheet, interactions):
        """Save interactions to a Google Sheet"""
        worksheet = spreadsheet.worksheet("Interactions")
        worksheet.clear()
        
        headers = ["contact_name", "interaction_type", "date", "notes", "follow_up_needed", "completed"]
        worksheet.append_row(headers)
        
        data = []
        for interaction in interactions:
            data.append([
                interaction.contact_name,
                interaction.interaction_type,
                interaction.date,
                interaction.notes,
                interaction.follow_up_needed,
                interaction.completed
            ])
        
        if data:
            worksheet.append_rows(data)
    
    def save_reminders_to_sheet(self, spreadsheet, reminders):
        """Save reminders to a Google Sheet"""
        worksheet = spreadsheet.worksheet("Reminders")
        worksheet.clear()
        
        if not reminders:
            return
        
        headers = list(reminders[0].keys())
        worksheet.append_row(headers)
        
        data = []
        for reminder in reminders:
            data.append([reminder[header] for header in headers])
        
        worksheet.append_rows(data)

class NetworkManager:
    """Enhanced NetworkManager with data persistence"""
    
    def __init__(self):
        self.contacts = []
        self.interactions = []
        self.csv_manager = CSVDataManager()
        self.sheets_manager = GoogleSheetsManager()
    
    def save_to_csv(self, contacts_file="contacts.csv", interactions_file="interactions.csv"):
        """Save all data to CSV files"""
        self.csv_manager.save_contacts(self.contacts, contacts_file)
        self.csv_manager.save_interactions(self.interactions, interactions_file)
    
    def load_from_csv(self, contacts_file="contacts.csv", interactions_file="interactions.csv"):
        """Load all data from CSV files"""
        self.contacts = self.csv_manager.load_contacts(contacts_file)
        # Note: Interactions would need to be loaded separately
    
    def save_to_google_sheets(self, spreadsheet_title="LinkedIn Network"):
        """Save all data to Google Sheets"""
        spreadsheet = self.sheets_manager.create_or_open_spreadsheet(spreadsheet_title)
        self.sheets_manager.save_contacts_to_sheet(spreadsheet, self.contacts)
        self.sheets_manager.save_interactions_to_sheet(spreadsheet, self.interactions)
    
    def load_from_google_sheets(self, spreadsheet_title="LinkedIn Network"):
        """Load all data from Google Sheets"""
        spreadsheet = self.sheets_manager.create_or_open_spreadsheet(spreadsheet_title)
        self.contacts = self.sheets_manager.load_contacts_from_sheet(spreadsheet)
        # Note: Interactions would need to be loaded separately
    
    # ... (rest of the existing methods remain the same)
```

## 🎯 **How to Use This System:**

### **1. Setup Google Sheets API:**
```bash
pip install gspread google-auth pandas
```

### **2. Create Google Service Account:**
1. Go to Google Cloud Console
2. Create a new project
3. Enable Google Sheets API
4. Create a service account
5. Download the JSON credentials file

### **3. Usage Examples:**

```python
# Initialize managers
manager = NetworkManager()
reminder_system = ReminderSystem()

# Connect to Google Sheets
manager.sheets_manager.connect("path/to/credentials.json")

# Add contacts and interactions
contact = LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology")
manager.add_contact(contact)

interaction = Interaction("Sarah Johnson", "Coffee Meeting", "2024-01-15", "Great conversation", True)
manager.add_interaction(interaction)

reminder_system.create_reminder("Sarah Johnson", "2024-01-25", "Follow up on meeting", "High")

# Save to Google Sheets
manager.save_to_google_sheets("My LinkedIn Network")

# Save to CSV as backup
manager.save_to_csv("backup_contacts.csv", "backup_interactions.csv")

# Load from Google Sheets
manager.load_from_google_sheets("My LinkedIn Network")

# Load from CSV
manager.load_from_csv("backup_contacts.csv", "backup_interactions.csv")
```

### **4. Google Sheets Structure:**
The system creates three worksheets:
- **Contacts**: All LinkedIn connections
- **Interactions**: All conversations and meetings
- **Reminders**: All follow-up tasks

This gives you the best of both worlds: easy CSV backup and powerful Google Sheets collaboration!

```python
import pytest
import pandas as pd
from unittest.mock import Mock, patch
from linkedin_network import (
    LinkedInContact, NetworkManager, Interaction, ReminderSystem,
    CSVDataManager, GoogleSheetsManager
)

class TestCSVDataManager:
    """Test CSV-based data storage and retrieval"""
    
    def test_save_contacts_to_csv(self, tmp_path):
        """Test saving contacts to a CSV file"""
        data_manager = CSVDataManager()
        manager = NetworkManager()
        
        # Add some contacts
        contact1 = LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology")
        contact2 = LinkedInContact("Mike Chen", "Product Manager", "Microsoft", "2024-01-15", "Technology")
        manager.add_contact(contact1)
        manager.add_contact(contact2)
        
        # Save to CSV
        csv_file = tmp_path / "contacts.csv"
        data_manager.save_contacts(manager.contacts, str(csv_file))
        
        # Verify file was created and contains data
        assert csv_file.exists()
        df = pd.read_csv(csv_file)
        assert len(df) == 2
        assert "Sarah Johnson" in df["name"].values
        assert "Mike Chen" in df["name"].values
    
    def test_load_contacts_from_csv(self, tmp_path):
        """Test loading contacts from a CSV file"""
        data_manager = CSVDataManager()
        
        # Create a test CSV file
        csv_file = tmp_path / "test_contacts.csv"
        test_data = {
            "name": ["Alice Smith", "Bob Johnson"],
            "title": ["Data Scientist", "Software Engineer"],
            "company": ["Netflix", "Amazon"],
            "connection_date": ["2024-01-01", "2024-01-02"],
            "industry": ["Entertainment", "Technology"],
            "connection_strength": [3, 4]
        }
        df = pd.DataFrame(test_data)
        df.to_csv(csv_file, index=False)
        
        # Load contacts
        contacts = data_manager.load_contacts(str(csv_file))
        
        assert len(contacts) == 2
        assert contacts[0].name == "Alice Smith"
        assert contacts[0].title == "Data Scientist"
        assert contacts[1].name == "Bob Johnson"
        assert contacts[1].company == "Amazon"
    
    def test_save_interactions_to_csv(self, tmp_path):
        """Test saving interactions to a CSV file"""
        data_manager = CSVDataManager()
        interactions = [
            Interaction("Sarah Johnson", "Coffee Meeting", "2024-01-15", "Great conversation", True),
            Interaction("Mike Chen", "LinkedIn Message", "2024-01-16", "Quick chat", False)
        ]
        
        csv_file = tmp_path / "interactions.csv"
        data_manager.save_interactions(interactions, str(csv_file))
        
        assert csv_file.exists()
        df = pd.read_csv(csv_file)
        assert len(df) == 2
        assert "Coffee Meeting" in df["interaction_type"].values
        assert "LinkedIn Message" in df["interaction_type"].values
    
    def test_save_reminders_to_csv(self, tmp_path):
        """Test saving reminders to a CSV file"""
        data_manager = CSVDataManager()
        reminder_system = ReminderSystem()
        
        reminder_system.create_reminder("Sarah Johnson", "2024-01-25", "Follow up on meeting", "High")
        reminder_system.create_reminder("Mike Chen", "2024-01-26", "Send thank you note", "Medium")
        
        csv_file = tmp_path / "reminders.csv"
        data_manager.save_reminders(reminder_system.reminders, str(csv_file))
        
        assert csv_file.exists()
        df = pd.read_csv(csv_file)
        assert len(df) == 2
        assert "Sarah Johnson" in df["contact_name"].values
        assert "High" in df["priority"].values

class TestGoogleSheetsManager:
    """Test Google Sheets integration for data storage"""
    
    @patch('gspread.authorize')
    def test_connect_to_google_sheets(self, mock_authorize):
        """Test connecting to Google Sheets"""
        sheets_manager = GoogleSheetsManager()
        
        # Mock the Google Sheets connection
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        sheets_manager.connect("path/to/credentials.json")
        
        assert sheets_manager.client is not None
        mock_authorize.assert_called_once()
    
    @patch('gspread.authorize')
    def test_create_or_open_spreadsheet(self, mock_authorize):
        """Test creating or opening a spreadsheet"""
        sheets_manager = GoogleSheetsManager()
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        # Mock spreadsheet operations
        mock_spreadsheet = Mock()
        mock_client.open.return_value = mock_spreadsheet
        mock_client.create.return_value = mock_spreadsheet
        
        sheets_manager.connect("path/to/credentials.json")
        
        # Test opening existing spreadsheet
        spreadsheet = sheets_manager.create_or_open_spreadsheet("LinkedIn Network")
        assert spreadsheet is not None
        
        # Test creating new spreadsheet
        mock_client.open.side_effect = Exception("Not found")
        spreadsheet = sheets_manager.create_or_open_spreadsheet("New Network")
        assert spreadsheet is not None
    
    @patch('gspread.authorize')
    def test_save_contacts_to_sheets(self, mock_authorize):
        """Test saving contacts to Google Sheets"""
        sheets_manager = GoogleSheetsManager()
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        mock_spreadsheet = Mock()
        mock_worksheet = Mock()
        mock_spreadsheet.worksheet.return_value = mock_worksheet
        mock_client.open.return_value = mock_spreadsheet
        
        sheets_manager.connect("path/to/credentials.json")
        spreadsheet = sheets_manager.create_or_open_spreadsheet("Test Network")
        
        # Create test contacts
        contacts = [
            LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology"),
            LinkedInContact("Mike Chen", "Product Manager", "Microsoft", "2024-01-15", "Technology")
        ]
        
        # Save contacts
        sheets_manager.save_contacts_to_sheet(spreadsheet, contacts)
        
        # Verify worksheet was accessed and data was updated
        mock_spreadsheet.worksheet.assert_called_with("Contacts")
        mock_worksheet.clear.assert_called_once()
        mock_worksheet.update.assert_called_once()
    
    @patch('gspread.authorize')
    def test_load_contacts_from_sheets(self, mock_authorize):
        """Test loading contacts from Google Sheets"""
        sheets_manager = GoogleSheetsManager()
        mock_client = Mock()
        mock_authorize.return_value = mock_client
        
        mock_spreadsheet = Mock()
        mock_worksheet = Mock()
        mock_spreadsheet.worksheet.return_value = mock_worksheet
        mock_client.open.return_value = mock_spreadsheet
        
        # Mock worksheet data
        mock_worksheet.get_all_records.return_value = [
            {
                "name": "Sarah Johnson",
                "title": "Engineering Manager",
                "company": "Google",
                "connection_date": "2024-01-10",
                "industry": "Technology",
                "connection_strength": 3
            },
            {
                "name": "Mike Chen",
                "title": "Product Manager",
                "company": "Microsoft",
                "connection_date": "2024-01-15",
                "industry": "Technology",
                "connection_strength": 4
            }
        ]
        
        sheets_manager.connect("path/to/credentials.json")
        spreadsheet = sheets_manager.create_or_open_spreadsheet("Test Network")
        
        # Load contacts
        contacts = sheets_manager.load_contacts_from_sheet(spreadsheet)
        
        assert len(contacts) == 2
        assert contacts[0].name == "Sarah Johnson"
        assert contacts[1].name == "Mike Chen"

class TestDataSync:
    """Test syncing data between different storage methods"""
    
    def test_sync_csv_to_sheets(self, tmp_path):
        """Test syncing data from CSV to Google Sheets"""
        # Create test CSV
        csv_file = tmp_path / "contacts.csv"
        test_data = {
            "name": ["Alice Smith", "Bob Johnson"],
            "title": ["Data Scientist", "Software Engineer"],
            "company": ["Netflix", "Amazon"],
            "connection_date": ["2024-01-01", "2024-01-02"],
            "industry": ["Entertainment", "Technology"],
            "connection_strength": [3, 4]
        }
        df = pd.DataFrame(test_data)
        df.to_csv(csv_file, index=False)
        
        # Load from CSV
        csv_manager = CSVDataManager()
        contacts = csv_manager.load_contacts(str(csv_file))
        
        # Mock Google Sheets sync
        with patch('gspread.authorize') as mock_authorize:
            sheets_manager = GoogleSheetsManager()
            mock_client = Mock()
            mock_authorize.return_value = mock_client
            
            mock_spreadsheet = Mock()
            mock_worksheet = Mock()
            mock_spreadsheet.worksheet.return_value = mock_worksheet
            mock_client.open.return_value = mock_spreadsheet
            
            sheets_manager.connect("path/to/credentials.json")
            spreadsheet = sheets_manager.create_or_open_spreadsheet("Synced Network")
            
            # Sync to sheets
            sheets_manager.save_contacts_to_sheet(spreadsheet, contacts)
            
            # Verify sync happened
            mock_worksheet.clear.assert_called_once()
            mock_worksheet.update.assert_called_once()
```

```python
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import os

class CSVDataManager:
    """Manages data storage and retrieval using CSV files"""
    
    def save_contacts(self, contacts, filepath):
        """Save contacts to a CSV file"""
        data = []
        for contact in contacts:
            data.append({
                "name": contact.name,
                "title": contact.title,
                "company": contact.company,
                "connection_date": contact.connection_date,
                "industry": contact.industry,
                "connection_strength": contact.connection_strength
            })
        
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
    
    def load_contacts(self, filepath):
        """Load contacts from a CSV file"""
        if not os.path.exists(filepath):
            return []
        
        df = pd.read_csv(filepath)
        contacts = []
        
        for _, row in df.iterrows():
            contact = LinkedInContact(
                name=row["name"],
                title=row["title"],
                company=row["company"],
                connection_date=row["connection_date"],
                industry=row["industry"],
                connection_strength=row["connection_strength"]
            )
            contacts.append(contact)
        
        return contacts
    
    def save_interactions(self, interactions, filepath):
        """Save interactions to a CSV file"""
        data = []
        for interaction in interactions:
            data.append({
                "contact_name": interaction.contact_name,
                "interaction_type": interaction.interaction_type,
                "date": interaction.date,
                "notes": interaction.notes,
                "follow_up_needed": interaction.follow_up_needed,
                "completed": interaction.completed
            })
        
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)
    
    def save_reminders(self, reminders, filepath):
        """Save reminders to a CSV file"""
        df = pd.DataFrame(reminders)
        df.to_csv(filepath, index=False)

class GoogleSheetsManager:
    """Manages data storage and retrieval using Google Sheets"""
    
    def __init__(self):
        self.client = None
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive'
        ]
    
    def connect(self, credentials_path):
        """Connect to Google Sheets API"""
        credentials = Credentials.from_service_account_file(
            credentials_path, scopes=self.scope
        )
        self.client = gspread.authorize(credentials)
    
    def create_or_open_spreadsheet(self, title):
        """Create a new spreadsheet or open existing one"""
        try:
            spreadsheet = self.client.open(title)
        except gspread.SpreadsheetNotFound:
            spreadsheet = self.client.create(title)
        return spreadsheet
    
    def save_contacts_to_sheet(self, spreadsheet, contacts):
        """Save contacts to a Google Sheet"""
        worksheet = spreadsheet.worksheet("Contacts")
        worksheet.clear()
        
        # Prepare headers
        headers = ["name", "title", "company", "connection_date", "industry", "connection_strength"]
        worksheet.append_row(headers)
        
        # Prepare data
        data = []
        for contact in contacts:
            data.append([
                contact.name,
                contact.title,
                contact.company,
                contact.connection_date,
                contact.industry,
                contact.connection_strength
            ])
        
        if data:
            worksheet.append_rows(data)
    
    def load_contacts_from_sheet(self, spreadsheet):
        """Load contacts from a Google Sheet"""
        try:
            worksheet = spreadsheet.worksheet("Contacts")
            records = worksheet.get_all_records()
            
            contacts = []
            for record in records:
                contact = LinkedInContact(
                    name=record["name"],
                    title=record["title"],
                    company=record["company"],
                    connection_date=record["connection_date"],
                    industry=record["industry"],
                    connection_strength=record["connection_strength"]
                )
                contacts.append(contact)
            
            return contacts
        except gspread.WorksheetNotFound:
            return []
    
    def save_interactions_to_sheet(self, spreadsheet, interactions):
        """Save interactions to a Google Sheet"""
        worksheet = spreadsheet.worksheet("Interactions")
        worksheet.clear()
        
        headers = ["contact_name", "interaction_type", "date", "notes", "follow_up_needed", "completed"]
        worksheet.append_row(headers)
        
        data = []
        for interaction in interactions:
            data.append([
                interaction.contact_name,
                interaction.interaction_type,
                interaction.date,
                interaction.notes,
                interaction.follow_up_needed,
                interaction.completed
            ])
        
        if data:
            worksheet.append_rows(data)
    
    def save_reminders_to_sheet(self, spreadsheet, reminders):
        """Save reminders to a Google Sheet"""
        worksheet = spreadsheet.worksheet("Reminders")
        worksheet.clear()
        
        if not reminders:
            return
        
        headers = list(reminders[0].keys())
        worksheet.append_row(headers)
        
        data = []
        for reminder in reminders:
            data.append([reminder[header] for header in headers])
        
        worksheet.append_rows(data)

class NetworkManager:
    """Enhanced NetworkManager with data persistence"""
    
    def __init__(self):
        self.contacts = []
        self.interactions = []
        self.csv_manager = CSVDataManager()
        self.sheets_manager = GoogleSheetsManager()
    
    def save_to_csv(self, contacts_file="contacts.csv", interactions_file="interactions.csv"):
        """Save all data to CSV files"""
        self.csv_manager.save_contacts(self.contacts, contacts_file)
        self.csv_manager.save_interactions(self.interactions, interactions_file)
    
    def load_from_csv(self, contacts_file="contacts.csv", interactions_file="interactions.csv"):
        """Load all data from CSV files"""
        self.contacts = self.csv_manager.load_contacts(contacts_file)
        # Note: Interactions would need to be loaded separately
    
    def save_to_google_sheets(self, spreadsheet_title="LinkedIn Network"):
        """Save all data to Google Sheets"""
        spreadsheet = self.sheets_manager.create_or_open_spreadsheet(spreadsheet_title)
        self.sheets_manager.save_contacts_to_sheet(spreadsheet, self.contacts)
        self.sheets_manager.save_interactions_to_sheet(spreadsheet, self.interactions)
    
    def load_from_google_sheets(self, spreadsheet_title="LinkedIn Network"):
        """Load all data from Google Sheets"""
        spreadsheet = self.sheets_manager.create_or_open_spreadsheet(spreadsheet_title)
        self.contacts = self.sheets_manager.load_contacts_from_sheet(spreadsheet)
        # Note: Interactions would need to be loaded separately
    
    # ... (rest of the existing methods remain the same)
```

```shellscript
pip install gspread google-auth pandas
```

```python
# Initialize managers
manager = NetworkManager()
reminder_system = ReminderSystem()

# Connect to Google Sheets
manager.sheets_manager.connect("path/to/credentials.json")

# Add contacts and interactions
contact = LinkedInContact("Sarah Johnson", "Engineering Manager", "Google", "2024-01-10", "Technology")
manager.add_contact(contact)

interaction = Interaction("Sarah Johnson", "Coffee Meeting", "2024-01-15", "Great conversation", True)
manager.add_interaction(interaction)

reminder_system.create_reminder("Sarah Johnson", "2024-01-25", "Follow up on meeting", "High")

# Save to Google Sheets
manager.save_to_google_sheets("My LinkedIn Network")

# Save to CSV as backup
manager.save_to_csv("backup_contacts.csv", "backup_interactions.csv")

# Load from Google Sheets
manager.load_from_google_sheets("My LinkedIn Network")

# Load from CSV
manager.load_from_csv("backup_contacts.csv", "backup_interactions.csv")
```

---

**User**

can we do a simple data scraper?

---

**Cursor**

Absolutely! A **Data Scraper** is perfect for your TDD exercise! It's:

- **Highly Practical**: Everyone needs to gather data from websites
- **Portfolio Gold**: Shows web scraping, data processing, and automation skills
- **TDD-Friendly**: Can build from basic URL fetching to sophisticated parsing
- **Real-world Value**: Useful for market research, job hunting, price monitoring

## �� **Data Scraper - 1 Week MVP Features**

### **Core Features:**
1. **URL Fetcher** - Download web pages safely
2. **HTML Parser** - Extract specific data from pages
3. **Data Cleaner** - Format and validate scraped data
4. **Batch Processor** - Handle multiple URLs
5. **Export System** - Save data to CSV/JSON

### **TDD Progression:**
- **RED-001**: Basic URL fetching and HTML retrieval
- **RED-002**: Simple HTML parsing and data extraction
- **RED-003**: Data cleaning and validation
- **RED-004**: Batch processing multiple URLs
- **RED-005**: Data export and storage

## �� **Let's Start with RED-001**

Here's the first test that will guide the GREEN team:

```python:data_scraper_test.py
import pytest
from unittest.mock import Mock, patch, mock_open
import requests
from data_scraper import WebScraper, URLFetcher

class TestURLFetcher:
    """Test the URLFetcher class that handles web requests"""
    
    def test_create_url_fetcher(self):
        """Test creating a URL fetcher with proper headers"""
        fetcher = URLFetcher()
        
        assert fetcher.headers is not None
        assert "User-Agent" in fetcher.headers
        assert "Accept" in fetcher.headers
        assert fetcher.timeout == 10  # Default timeout
    
    def test_fetch_valid_url(self):
        """Test fetching content from a valid URL"""
        fetcher = URLFetcher()
        
        # Mock the requests.get response
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = "<html><body><h1>Test Page</h1></body></html>"
            mock_response.encoding = 'utf-8'
            mock_get.return_value = mock_response
            
            content = fetcher.fetch_url("https://example.com")
            
            assert content is not None
            assert "<html>" in content
            assert "<h1>Test Page</h1>" in content
            mock_get.assert_called_once()
    
    def test_fetch_invalid_url(self):
        """Test handling of invalid URLs"""
        fetcher = URLFetcher()
        
        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException("Invalid URL")
            
            content = fetcher.fetch_url("https://invalid-url-that-does-not-exist.com")
            
            assert content is None
    
    def test_fetch_url_with_timeout(self):
        """Test URL fetching with custom timeout"""
        fetcher = URLFetcher(timeout=5)
        
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = "Test content"
            mock_response.encoding = 'utf-8'
            mock_get.return_value = mock_response
            
            fetcher.fetch_url("https://example.com")
            
            # Verify timeout was used
            mock_get.assert_called_once()
            call_args = mock_get.call_args
            assert call_args[1]['timeout'] == 5
    
    def test_fetch_url_with_custom_headers(self):
        """Test URL fetching with custom headers"""
        custom_headers = {
            "User-Agent": "My Custom Bot/1.0",
            "Accept": "text/html,application/xhtml+xml"
        }
        fetcher = URLFetcher(headers=custom_headers)
        
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = "Test content"
            mock_response.encoding = 'utf-8'
            mock_get.return_value = mock_response
            
            fetcher.fetch_url("https://example.com")
            
            # Verify custom headers were used
            mock_get.assert_called_once()
            call_args = mock_get.call_args
            assert call_args[1]['headers'] == custom_headers

class TestWebScraper:
    """Test the main WebScraper class"""
    
    def test_create_web_scraper(self):
        """Test creating a web scraper instance"""
        scraper = WebScraper()
        
        assert scraper.fetcher is not None
        assert isinstance(scraper.fetcher, URLFetcher)
        assert scraper.scraped_data == []
    
    def test_scrape_single_url(self):
        """Test scraping a single URL"""
        scraper = WebScraper()
        
        test_html = """
        <html>
            <body>
                <h1>Job Title: Software Engineer</h1>
                <p>Company: Google</p>
                <p>Location: Mountain View, CA</p>
                <p>Salary: $150,000</p>
            </body>
        </html>
        """
        
        with patch.object(scraper.fetcher, 'fetch_url') as mock_fetch:
            mock_fetch.return_value = test_html
            
            result = scraper.scrape_url("https://example.com/job-posting")
            
            assert result is not None
            assert result['url'] == "https://example.com/job-posting"
            assert result['content'] == test_html
            assert result['status'] == 'success'
    
    def test_scrape_url_with_error(self):
        """Test scraping a URL that fails"""
        scraper = WebScraper()
        
        with patch.object(scraper.fetcher, 'fetch_url') as mock_fetch:
            mock_fetch.return_value = None
            
            result = scraper.scrape_url("https://invalid-url.com")
            
            assert result is not None
            assert result['url'] == "https://invalid-url.com"
            assert result['status'] == 'error'
            assert result['content'] is None
    
    def test_scrape_multiple_urls(self):
        """Test scraping multiple URLs"""
        scraper = WebScraper()
        
        urls = [
            "https://example.com/page1",
            "https://example.com/page2",
            "https://example.com/page3"
        ]
        
        with patch.object(scraper.fetcher, 'fetch_url') as mock_fetch:
            mock_fetch.side_effect = [
                "<html><body>Page 1</body></html>",
                "<html><body>Page 2</body></html>",
                "<html><body>Page 3</body></html>"
            ]
            
            results = scraper.scrape_urls(urls)
            
            assert len(results) == 3
            assert all(result['status'] == 'success' for result in results)
            assert results[0]['content'] == "<html><body>Page 1</body></html>"
            assert results[1]['content'] == "<html><body>Page 2</body></html>"
            assert results[2]['content'] == "<html><body>Page 3</body></html>"
    
    def test_get_scraped_data(self):
        """Test retrieving all scraped data"""
        scraper = WebScraper()
        
        # Add some test data
        scraper.scraped_data = [
            {'url': 'https://example1.com', 'content': 'Content 1', 'status': 'success'},
            {'url': 'https://example2.com', 'content': 'Content 2', 'status': 'success'}
        ]
        
        data = scraper.get_scraped_data()
        
        assert len(data) == 2
        assert data[0]['url'] == 'https://example1.com'
        assert data[1]['url'] == 'https://example2.com'
    
    def test_clear_scraped_data(self):
        """Test clearing all scraped data"""
        scraper = WebScraper()
        
        # Add some test data
        scraper.scraped_data = [
            {'url': 'https://example1.com', 'content': 'Content 1', 'status': 'success'}
        ]
        
        scraper.clear_data()
        
        assert len(scraper.scraped_data) == 0
```

And here's the corresponding implementation:

```python:data_scraper.py
import requests
from datetime import datetime
import time

class URLFetcher:
    """Handles fetching content from URLs"""
    
    def __init__(self, timeout=10, headers=None):
        self.timeout = timeout
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }
    
    def fetch_url(self, url):
        """Fetch content from a URL"""
        try:
            response = requests.get(
                url, 
                headers=self.headers, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

class WebScraper:
    """Main web scraper class"""
    
    def __init__(self, delay=1):
        self.fetcher = URLFetcher()
        self.scraped_data = []
        self.delay = delay  # Delay between requests to be respectful
    
    def scrape_url(self, url):
        """Scrape a single URL"""
        print(f"Scraping: {url}")
        
        content = self.fetcher.fetch_url(url)
        
        result = {
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'status': 'success' if content else 'error',
            'content': content
        }
        
        self.scraped_data.append(result)
        return result
    
    def scrape_urls(self, urls):
        """Scrape multiple URLs with delay between requests"""
        results = []
        
        for url in urls:
            result = self.scrape_url(url)
            results.append(result)
            
            # Be respectful with delays
            if self.delay > 0:
                time.sleep(self.delay)
        
        return results
    
    def get_scraped_data(self):
        """Get all scraped data"""
        return self.scraped_data
    
    def clear_data(self):
        """Clear all scraped data"""
        self.scraped_data = []
    
    def get_successful_scrapes(self):
        """Get only successful scrapes"""
        return [data for data in self.scraped_data if data['status'] == 'success']
    
    def get_failed_scrapes(self):
        """Get only failed scrapes"""
        return [data for data in self.scraped_data if data['status'] == 'error']
```

## 🎯 **What This RED-001 Test Reveals:**

The GREEN team will discover they're building:
- A web scraping system
- URL fetching with proper headers and error handling
- Support for multiple URLs with delays
- Data storage and retrieval

**But they won't know yet about:**
- HTML parsing and data extraction
- Data cleaning and validation
- Export functionality
- Advanced parsing techniques

## 🚀 **Usage Example:**

```python
# Basic usage
scraper = WebScraper(delay=2)  # 2 second delay between requests

# Scrape a single URL
result = scraper.scrape_url("https://example.com")
print(f"Status: {result['status']}")
print(f"Content length: {len(result['content']) if result['content'] else 0}")

# Scrape multiple URLs
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

results = scraper.scrape_urls(urls)
print(f"Successfully scraped: {len(scraper.get_successful_scrapes())}")
print(f"Failed scrapes: {len(scraper.get_failed_scrapes())}")

# Get all data
all_data = scraper.get_scraped_data()
```

This creates a solid foundation for a data scraper! Each subsequent RED branch will add more sophisticated parsing and data processing capabilities.

Would you like me to create the RED-002 test that would add HTML parsing functionality?

```python
import pytest
from unittest.mock import Mock, patch, mock_open
import requests
from data_scraper import WebScraper, URLFetcher

class TestURLFetcher:
    """Test the URLFetcher class that handles web requests"""
    
    def test_create_url_fetcher(self):
        """Test creating a URL fetcher with proper headers"""
        fetcher = URLFetcher()
        
        assert fetcher.headers is not None
        assert "User-Agent" in fetcher.headers
        assert "Accept" in fetcher.headers
        assert fetcher.timeout == 10  # Default timeout
    
    def test_fetch_valid_url(self):
        """Test fetching content from a valid URL"""
        fetcher = URLFetcher()
        
        # Mock the requests.get response
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = "<html><body><h1>Test Page</h1></body></html>"
            mock_response.encoding = 'utf-8'
            mock_get.return_value = mock_response
            
            content = fetcher.fetch_url("https://example.com")
            
            assert content is not None
            assert "<html>" in content
            assert "<h1>Test Page</h1>" in content
            mock_get.assert_called_once()
    
    def test_fetch_invalid_url(self):
        """Test handling of invalid URLs"""
        fetcher = URLFetcher()
        
        with patch('requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException("Invalid URL")
            
            content = fetcher.fetch_url("https://invalid-url-that-does-not-exist.com")
            
            assert content is None
    
    def test_fetch_url_with_timeout(self):
        """Test URL fetching with custom timeout"""
        fetcher = URLFetcher(timeout=5)
        
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = "Test content"
            mock_response.encoding = 'utf-8'
            mock_get.return_value = mock_response
            
            fetcher.fetch_url("https://example.com")
            
            # Verify timeout was used
            mock_get.assert_called_once()
            call_args = mock_get.call_args
            assert call_args[1]['timeout'] == 5
    
    def test_fetch_url_with_custom_headers(self):
        """Test URL fetching with custom headers"""
        custom_headers = {
            "User-Agent": "My Custom Bot/1.0",
            "Accept": "text/html,application/xhtml+xml"
        }
        fetcher = URLFetcher(headers=custom_headers)
        
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = "Test content"
            mock_response.encoding = 'utf-8'
            mock_get.return_value = mock_response
            
            fetcher.fetch_url("https://example.com")
            
            # Verify custom headers were used
            mock_get.assert_called_once()
            call_args = mock_get.call_args
            assert call_args[1]['headers'] == custom_headers

class TestWebScraper:
    """Test the main WebScraper class"""
    
    def test_create_web_scraper(self):
        """Test creating a web scraper instance"""
        scraper = WebScraper()
        
        assert scraper.fetcher is not None
        assert isinstance(scraper.fetcher, URLFetcher)
        assert scraper.scraped_data == []
    
    def test_scrape_single_url(self):
        """Test scraping a single URL"""
        scraper = WebScraper()
        
        test_html = """
        <html>
            <body>
                <h1>Job Title: Software Engineer</h1>
                <p>Company: Google</p>
                <p>Location: Mountain View, CA</p>
                <p>Salary: $150,000</p>
            </body>
        </html>
        """
        
        with patch.object(scraper.fetcher, 'fetch_url') as mock_fetch:
            mock_fetch.return_value = test_html
            
            result = scraper.scrape_url("https://example.com/job-posting")
            
            assert result is not None
            assert result['url'] == "https://example.com/job-posting"
            assert result['content'] == test_html
            assert result['status'] == 'success'
    
    def test_scrape_url_with_error(self):
        """Test scraping a URL that fails"""
        scraper = WebScraper()
        
        with patch.object(scraper.fetcher, 'fetch_url') as mock_fetch:
            mock_fetch.return_value = None
            
            result = scraper.scrape_url("https://invalid-url.com")
            
            assert result is not None
            assert result['url'] == "https://invalid-url.com"
            assert result['status'] == 'error'
            assert result['content'] is None
    
    def test_scrape_multiple_urls(self):
        """Test scraping multiple URLs"""
        scraper = WebScraper()
        
        urls = [
            "https://example.com/page1",
            "https://example.com/page2",
            "https://example.com/page3"
        ]
        
        with patch.object(scraper.fetcher, 'fetch_url') as mock_fetch:
            mock_fetch.side_effect = [
                "<html><body>Page 1</body></html>",
                "<html><body>Page 2</body></html>",
                "<html><body>Page 3</body></html>"
            ]
            
            results = scraper.scrape_urls(urls)
            
            assert len(results) == 3
            assert all(result['status'] == 'success' for result in results)
            assert results[0]['content'] == "<html><body>Page 1</body></html>"
            assert results[1]['content'] == "<html><body>Page 2</body></html>"
            assert results[2]['content'] == "<html><body>Page 3</body></html>"
    
    def test_get_scraped_data(self):
        """Test retrieving all scraped data"""
        scraper = WebScraper()
        
        # Add some test data
        scraper.scraped_data = [
            {'url': 'https://example1.com', 'content': 'Content 1', 'status': 'success'},
            {'url': 'https://example2.com', 'content': 'Content 2', 'status': 'success'}
        ]
        
        data = scraper.get_scraped_data()
        
        assert len(data) == 2
        assert data[0]['url'] == 'https://example1.com'
        assert data[1]['url'] == 'https://example2.com'
    
    def test_clear_scraped_data(self):
        """Test clearing all scraped data"""
        scraper = WebScraper()
        
        # Add some test data
        scraper.scraped_data = [
            {'url': 'https://example1.com', 'content': 'Content 1', 'status': 'success'}
        ]
        
        scraper.clear_data()
        
        assert len(scraper.scraped_data) == 0
```

```python
import requests
from datetime import datetime
import time

class URLFetcher:
    """Handles fetching content from URLs"""
    
    def __init__(self, timeout=10, headers=None):
        self.timeout = timeout
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
        }
    
    def fetch_url(self, url):
        """Fetch content from a URL"""
        try:
            response = requests.get(
                url, 
                headers=self.headers, 
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None

class WebScraper:
    """Main web scraper class"""
    
    def __init__(self, delay=1):
        self.fetcher = URLFetcher()
        self.scraped_data = []
        self.delay = delay  # Delay between requests to be respectful
    
    def scrape_url(self, url):
        """Scrape a single URL"""
        print(f"Scraping: {url}")
        
        content = self.fetcher.fetch_url(url)
        
        result = {
            'url': url,
            'timestamp': datetime.now().isoformat(),
            'status': 'success' if content else 'error',
            'content': content
        }
        
        self.scraped_data.append(result)
        return result
    
    def scrape_urls(self, urls):
        """Scrape multiple URLs with delay between requests"""
        results = []
        
        for url in urls:
            result = self.scrape_url(url)
            results.append(result)
            
            # Be respectful with delays
            if self.delay > 0:
                time.sleep(self.delay)
        
        return results
    
    def get_scraped_data(self):
        """Get all scraped data"""
        return self.scraped_data
    
    def clear_data(self):
        """Clear all scraped data"""
        self.scraped_data = []
    
    def get_successful_scrapes(self):
        """Get only successful scrapes"""
        return [data for data in self.scraped_data if data['status'] == 'success']
    
    def get_failed_scrapes(self):
        """Get only failed scrapes"""
        return [data for data in self.scraped_data if data['status'] == 'error']
```

```python
# Basic usage
scraper = WebScraper(delay=2)  # 2 second delay between requests

# Scrape a single URL
result = scraper.scrape_url("https://example.com")
print(f"Status: {result['status']}")
print(f"Content length: {len(result['content']) if result['content'] else 0}")

# Scrape multiple URLs
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3"
]

results = scraper.scrape_urls(urls)
print(f"Successfully scraped: {len(scraper.get_successful_scrapes())}")
print(f"Failed scrapes: {len(scraper.get_failed_scrapes())}")

# Get all data
all_data = scraper.get_scraped_data()
```

---

**User**

what would be something along these lines that would be simpler for a beginner to come up with?

---

**Cursor**

Great question! Let me suggest some **much simpler** data scraping projects that would be perfect for beginners while still being impressive:

## �� **Simple Data Scraper Ideas for Beginners**

### **1. Weather Data Collector** 🌤️
**Why it's perfect for beginners:**
- **Simple Structure**: Most weather sites have predictable HTML
- **Clear Data**: Temperature, conditions, dates are easy to find
- **No Complex Logic**: Just extract numbers and text
- **Immediate Value**: Everyone understands weather data

**TDD Progression:**
- **RED-001**: Fetch weather page HTML
- **RED-002**: Extract temperature and conditions
- **RED-003**: Parse multiple days of forecast
- **RED-004**: Save data to CSV
- **RED-005**: Compare temperatures across cities

### **2. News Headline Scraper** ��
**Why it's perfect for beginners:**
- **Simple HTML**: Headlines are usually in `<h1>`, `<h2>`, or `<h3>` tags
- **Clear Patterns**: Title, date, maybe category
- **No Complex Parsing**: Just text extraction
- **Universal Appeal**: Everyone reads news

**TDD Progression:**
- **RED-001**: Fetch news website HTML
- **RED-002**: Extract headlines from specific tags
- **RED-003**: Get headline dates and categories
- **RED-004**: Filter headlines by keywords
- **RED-005**: Save headlines to file

### **3. Product Price Tracker** ��
**Why it's perfect for beginners:**
- **Simple Goal**: Find price numbers on a page
- **Clear Data**: Price, product name, maybe availability
- **Limited Scope**: One product or category
- **Practical Use**: Everyone wants to track prices

**TDD Progression:**
- **RED-001**: Fetch product page HTML
- **RED-002**: Extract price and product name
- **RED-003**: Check if product is in stock
- **RED-004**: Track price changes over time
- **RED-005**: Alert when price drops

## 🏆 **My Top Recommendation: Weather Data Collector**

Here's a **RED-001** test that would be perfect for beginners:

```python:weather_scraper_test.py
import pytest
from unittest.mock import Mock, patch
from weather_scraper import WeatherScraper

class TestWeatherScraper:
    """Test the weather scraper for beginners"""
    
    def test_create_weather_scraper(self):
        """Test creating a weather scraper"""
        scraper = WeatherScraper()
        
        assert scraper.base_url is not None
        assert scraper.weather_data == []
    
    def test_fetch_weather_page(self):
        """Test fetching a weather page"""
        scraper = WeatherScraper()
        
        # Mock HTML response
        test_html = """
        <html>
            <body>
                <div class="temperature">72°F</div>
                <div class="condition">Sunny</div>
                <div class="location">New York, NY</div>
            </body>
        </html>
        """
        
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = test_html
            mock_get.return_value = mock_response
            
            content = scraper.fetch_weather_page("New York")
            
            assert content is not None
            assert "72°F" in content
            assert "Sunny" in content
    
    def test_extract_temperature(self):
        """Test extracting temperature from HTML"""
        scraper = WeatherScraper()
        
        html_content = '<div class="temperature">72°F</div>'
        temperature = scraper.extract_temperature(html_content)
        
        assert temperature == "72°F"
    
    def test_extract_condition(self):
        """Test extracting weather condition from HTML"""
        scraper = WeatherScraper()
        
        html_content = '<div class="condition">Partly Cloudy</div>'
        condition = scraper.extract_condition(html_content)
        
        assert condition == "Partly Cloudy"
    
    def test_scrape_weather_for_city(self):
        """Test scraping weather for a specific city"""
        scraper = WeatherScraper()
        
        test_html = """
        <html>
            <body>
                <div class="temperature">65°F</div>
                <div class="condition">Rainy</div>
                <div class="location">Seattle, WA</div>
            </body>
        </html>
        """
        
        with patch.object(scraper, 'fetch_weather_page') as mock_fetch:
            mock_fetch.return_value = test_html
            
            weather_info = scraper.scrape_weather("Seattle")
            
            assert weather_info is not None
            assert weather_info['city'] == "Seattle"
            assert weather_info['temperature'] == "65°F"
            assert weather_info['condition'] == "Rainy"
    
    def test_scrape_multiple_cities(self):
        """Test scraping weather for multiple cities"""
        scraper = WeatherScraper()
        
        cities = ["New York", "Los Angeles", "Chicago"]
        
        with patch.object(scraper, 'fetch_weather_page') as mock_fetch:
            mock_fetch.side_effect = [
                '<div class="temperature">72°F</div><div class="condition">Sunny</div>',
                '<div class="temperature">75°F</div><div class="condition">Clear</div>',
                '<div class="temperature">45°F</div><div class="condition">Cold</div>'
            ]
            
            results = scraper.scrape_multiple_cities(cities)
            
            assert len(results) == 3
            assert results[0]['city'] == "New York"
            assert results[1]['city'] == "Los Angeles"
            assert results[2]['city'] == "Chicago"
```

And the simple implementation:

```python:weather_scraper.py
import requests
import re
from datetime import datetime

class WeatherScraper:
    """Simple weather scraper for beginners"""
    
    def __init__(self):
        self.base_url = "https://weather.com"  # Example URL
        self.weather_data = []
    
    def fetch_weather_page(self, city):
        """Fetch weather page for a city"""
        try:
            url = f"{self.base_url}/weather/{city}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather for {city}: {e}")
            return None
    
    def extract_temperature(self, html_content):
        """Extract temperature from HTML"""
        # Simple regex to find temperature
        temp_match = re.search(r'(\d+°F)', html_content)
        return temp_match.group(1) if temp_match else "Unknown"
    
    def extract_condition(self, html_content):
        """Extract weather condition from HTML"""
        # Simple regex to find condition
        condition_match = re.search(r'<div class="condition">([^<]+)</div>', html_content)
        return condition_match.group(1) if condition_match else "Unknown"
    
    def scrape_weather(self, city):
        """Scrape weather for a specific city"""
        print(f"Scraping weather for {city}...")
        
        html_content = self.fetch_weather_page(city)
        if not html_content:
            return None
        
        weather_info = {
            'city': city,
            'temperature': self.extract_temperature(html_content),
            'condition': self.extract_condition(html_content),
            'timestamp': datetime.now().isoformat()
        }
        
        self.weather_data.append(weather_info)
        return weather_info
    
    def scrape_multiple_cities(self, cities):
        """Scrape weather for multiple cities"""
        results = []
        for city in cities:
            result = self.scrape_weather(city)
            if result:
                results.append(result)
        return results
    
    def get_weather_data(self):
        """Get all scraped weather data"""
        return self.weather_data
    
    def find_hottest_city(self):
        """Find the city with the highest temperature"""
        if not self.weather_data:
            return None
        
        hottest = max(self.weather_data, 
                     key=lambda x: int(x['temperature'].replace('°F', '')))
        return hottest
```

## 🎯 **Why This is Perfect for Beginners:**

### **Simple Concepts:**
1. **Basic HTML**: Just find `<div>` tags with specific classes
2. **Simple Regex**: Extract numbers and text patterns
3. **Clear Data**: Temperature, condition, city name
4. **No Complex Logic**: Just extract and store

### **Immediate Success:**
- Works with any weather website
- Results are immediately understandable
- Can be extended easily
- Shows real-world application

### **Learning Progression:**
- **RED-001**: Basic HTML fetching
- **RED-002**: Simple text extraction
- **RED-003**: Multiple cities
- **RED-004**: Data comparison
- **RED-005**: Save to file

## 🚀 **Usage Example:**

```python
# Super simple usage
scraper = WeatherScraper()

# Scrape one city
weather = scraper.scrape_weather("New York")
print(f"Temperature in {weather['city']}: {weather['temperature']}")

# Scrape multiple cities
cities = ["New York", "Los Angeles", "Chicago"]
results = scraper.scrape_multiple_cities(cities)

# Find hottest city
hottest = scraper.find_hottest_city()
print(f"Hottest city: {hottest['city']} at {hottest['temperature']}")
```

This is much more approachable for beginners while still being impressive and useful! Would you like me to show the RED-002 test that would add more sophisticated parsing?

```python
import pytest
from unittest.mock import Mock, patch
from weather_scraper import WeatherScraper

class TestWeatherScraper:
    """Test the weather scraper for beginners"""
    
    def test_create_weather_scraper(self):
        """Test creating a weather scraper"""
        scraper = WeatherScraper()
        
        assert scraper.base_url is not None
        assert scraper.weather_data == []
    
    def test_fetch_weather_page(self):
        """Test fetching a weather page"""
        scraper = WeatherScraper()
        
        # Mock HTML response
        test_html = """
        <html>
            <body>
                <div class="temperature">72°F</div>
                <div class="condition">Sunny</div>
                <div class="location">New York, NY</div>
            </body>
        </html>
        """
        
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = test_html
            mock_get.return_value = mock_response
            
            content = scraper.fetch_weather_page("New York")
            
            assert content is not None
            assert "72°F" in content
            assert "Sunny" in content
    
    def test_extract_temperature(self):
        """Test extracting temperature from HTML"""
        scraper = WeatherScraper()
        
        html_content = '<div class="temperature">72°F</div>'
        temperature = scraper.extract_temperature(html_content)
        
        assert temperature == "72°F"
    
    def test_extract_condition(self):
        """Test extracting weather condition from HTML"""
        scraper = WeatherScraper()
        
        html_content = '<div class="condition">Partly Cloudy</div>'
        condition = scraper.extract_condition(html_content)
        
        assert condition == "Partly Cloudy"
    
    def test_scrape_weather_for_city(self):
        """Test scraping weather for a specific city"""
        scraper = WeatherScraper()
        
        test_html = """
        <html>
            <body>
                <div class="temperature">65°F</div>
                <div class="condition">Rainy</div>
                <div class="location">Seattle, WA</div>
            </body>
        </html>
        """
        
        with patch.object(scraper, 'fetch_weather_page') as mock_fetch:
            mock_fetch.return_value = test_html
            
            weather_info = scraper.scrape_weather("Seattle")
            
            assert weather_info is not None
            assert weather_info['city'] == "Seattle"
            assert weather_info['temperature'] == "65°F"
            assert weather_info['condition'] == "Rainy"
    
    def test_scrape_multiple_cities(self):
        """Test scraping weather for multiple cities"""
        scraper = WeatherScraper()
        
        cities = ["New York", "Los Angeles", "Chicago"]
        
        with patch.object(scraper, 'fetch_weather_page') as mock_fetch:
            mock_fetch.side_effect = [
                '<div class="temperature">72°F</div><div class="condition">Sunny</div>',
                '<div class="temperature">75°F</div><div class="condition">Clear</div>',
                '<div class="temperature">45°F</div><div class="condition">Cold</div>'
            ]
            
            results = scraper.scrape_multiple_cities(cities)
            
            assert len(results) == 3
            assert results[0]['city'] == "New York"
            assert results[1]['city'] == "Los Angeles"
            assert results[2]['city'] == "Chicago"
```

```python
import requests
import re
from datetime import datetime

class WeatherScraper:
    """Simple weather scraper for beginners"""
    
    def __init__(self):
        self.base_url = "https://weather.com"  # Example URL
        self.weather_data = []
    
    def fetch_weather_page(self, city):
        """Fetch weather page for a city"""
        try:
            url = f"{self.base_url}/weather/{city}"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather for {city}: {e}")
            return None
    
    def extract_temperature(self, html_content):
        """Extract temperature from HTML"""
        # Simple regex to find temperature
        temp_match = re.search(r'(\d+°F)', html_content)
        return temp_match.group(1) if temp_match else "Unknown"
    
    def extract_condition(self, html_content):
        """Extract weather condition from HTML"""
        # Simple regex to find condition
        condition_match = re.search(r'<div class="condition">([^<]+)</div>', html_content)
        return condition_match.group(1) if condition_match else "Unknown"
    
    def scrape_weather(self, city):
        """Scrape weather for a specific city"""
        print(f"Scraping weather for {city}...")
        
        html_content = self.fetch_weather_page(city)
        if not html_content:
            return None
        
        weather_info = {
            'city': city,
            'temperature': self.extract_temperature(html_content),
            'condition': self.extract_condition(html_content),
            'timestamp': datetime.now().isoformat()
        }
        
        self.weather_data.append(weather_info)
        return weather_info
    
    def scrape_multiple_cities(self, cities):
        """Scrape weather for multiple cities"""
        results = []
        for city in cities:
            result = self.scrape_weather(city)
            if result:
                results.append(result)
        return results
    
    def get_weather_data(self):
        """Get all scraped weather data"""
        return self.weather_data
    
    def find_hottest_city(self):
        """Find the city with the highest temperature"""
        if not self.weather_data:
            return None
        
        hottest = max(self.weather_data, 
                     key=lambda x: int(x['temperature'].replace('°F', '')))
        return hottest
```

```python
# Super simple usage
scraper = WeatherScraper()

# Scrape one city
weather = scraper.scrape_weather("New York")
print(f"Temperature in {weather['city']}: {weather['temperature']}")

# Scrape multiple cities
cities = ["New York", "Los Angeles", "Chicago"]
results = scraper.scrape_multiple_cities(cities)

# Find hottest city
hottest = scraper.find_hottest_city()
print(f"Hottest city: {hottest['city']} at {hottest['temperature']}")
```

---

**User**

no no - I'm looking for simpler ideas for job hnt or market analysis that can be created using simple loops, functions, and math. nothing too complex, and keep libraries to a minimum. no Mocking required for the testing please, just straight PYTESTS

---

**Cursor**

Ah, perfect! You want **simple, math-based job hunt/market analysis tools** with minimal dependencies. Here are some excellent beginner-friendly ideas:

## 🎯 **Simple Job Hunt/Market Analysis Tools**

### **1. Salary Calculator** ��
**Why it's perfect:**
- **Simple Math**: Basic arithmetic and averages
- **No External APIs**: Just calculations
- **Immediate Value**: Everyone needs salary insights
- **TDD-Friendly**: Clear input/output relationships

**Features:**
- Calculate average salary from a list
- Compare your salary to market average
- Calculate salary ranges (min, max, median)
- Adjust for experience level

### **2. Job Application Tracker** ��
**Why it's perfect:**
- **Simple Data**: Just lists and dictionaries
- **Basic Math**: Success rates, averages
- **No Complex Logic**: Add, count, calculate percentages
- **Real-world Useful**: Track your job hunt progress

**Features:**
- Track applications and outcomes
- Calculate success rates
- Find average time to response
- Identify best performing companies

### **3. Skills Gap Analyzer** ��
**Why it's perfect:**
- **Simple Matching**: Compare two lists
- **Basic Math**: Count matches, calculate percentages
- **No External Dependencies**: Just Python lists
- **Portfolio Gold**: Shows analytical thinking

**Features:**
- Compare your skills to job requirements
- Calculate match percentage
- Identify missing skills
- Prioritize skill development

## 🏆 **My Top Recommendation: Salary Calculator**

Here's a **RED-001** test that's perfect for beginners:

```python:salary_calculator_test.py
import pytest
from salary_calculator import SalaryCalculator

class TestSalaryCalculator:
    """Test the salary calculator for job market analysis"""
    
    def test_create_salary_calculator(self):
        """Test creating a salary calculator"""
        calculator = SalaryCalculator()
        
        assert calculator.salaries == []
        assert calculator.job_title == ""
    
    def test_add_salary(self):
        """Test adding a salary to the calculator"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(75000, "Software Engineer", "Google")
        
        assert len(calculator.salaries) == 1
        assert calculator.salaries[0]["amount"] == 75000
        assert calculator.salaries[0]["title"] == "Software Engineer"
        assert calculator.salaries[0]["company"] == "Google"
    
    def test_calculate_average_salary(self):
        """Test calculating average salary"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(70000, "Developer", "Company A")
        calculator.add_salary(80000, "Developer", "Company B")
        calculator.add_salary(90000, "Developer", "Company C")
        
        average = calculator.calculate_average_salary()
        
        assert average == 80000  # (70000 + 80000 + 90000) / 3
    
    def test_calculate_average_with_no_salaries(self):
        """Test calculating average with no data"""
        calculator = SalaryCalculator()
        
        average = calculator.calculate_average_salary()
        
        assert average == 0
    
    def test_find_salary_range(self):
        """Test finding min and max salaries"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(60000, "Developer", "Company A")
        calculator.add_salary(85000, "Developer", "Company B")
        calculator.add_salary(95000, "Developer", "Company C")
        
        salary_range = calculator.find_salary_range()
        
        assert salary_range["min"] == 60000
        assert salary_range["max"] == 95000
        assert salary_range["range"] == 35000  # 95000 - 60000
    
    def test_compare_salary_to_market(self):
        """Test comparing your salary to market average"""
        calculator = SalaryCalculator()
        
        # Add market data
        calculator.add_salary(70000, "Developer", "Company A")
        calculator.add_salary(80000, "Developer", "Company B")
        calculator.add_salary(90000, "Developer", "Company C")
        
        # Compare your salary
        comparison = calculator.compare_salary_to_market(75000)
        
        assert comparison["your_salary"] == 75000
        assert comparison["market_average"] == 80000
        assert comparison["difference"] == -5000  # 75000 - 80000
        assert comparison["percentage"] == -6.25  # (-5000 / 80000) * 100
    
    def test_calculate_salary_by_experience(self):
        """Test calculating salary based on experience level"""
        calculator = SalaryCalculator()
        
        # Add salaries with experience levels
        calculator.add_salary_with_experience(60000, "Developer", "Company A", 1)
        calculator.add_salary_with_experience(80000, "Developer", "Company B", 3)
        calculator.add_salary_with_experience(100000, "Developer", "Company C", 5)
        
        # Calculate average for 3 years experience
        avg_3_years = calculator.calculate_average_by_experience(3)
        
        assert avg_3_years == 80000
    
    def test_get_companies_above_average(self):
        """Test finding companies that pay above average"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(70000, "Developer", "Company A")
        calculator.add_salary(80000, "Developer", "Company B")
        calculator.add_salary(90000, "Developer", "Company C")
        calculator.add_salary(95000, "Developer", "Company D")
        
        above_average = calculator.get_companies_above_average()
        
        assert len(above_average) == 2  # Company C and D
        assert "Company C" in above_average
        assert "Company D" in above_average
    
    def test_calculate_salary_percentile(self):
        """Test calculating salary percentile"""
        calculator = SalaryCalculator()
        
        # Add 10 salaries
        for i in range(10):
            calculator.add_salary(50000 + (i * 5000), "Developer", f"Company {i}")
        
        # Test 50th percentile (median)
        median = calculator.calculate_salary_percentile(50)
        assert median == 72500  # Middle value
        
        # Test 75th percentile
        percentile_75 = calculator.calculate_salary_percentile(75)
        assert percentile_75 == 87500  # 75% of values are below this
```

And the simple implementation:

```python:salary_calculator.py
class SalaryCalculator:
    """Simple salary calculator for job market analysis"""
    
    def __init__(self):
        self.salaries = []
        self.job_title = ""
    
    def add_salary(self, amount, title, company):
        """Add a salary to the calculator"""
        salary_data = {
            "amount": amount,
            "title": title,
            "company": company
        }
        self.salaries.append(salary_data)
    
    def add_salary_with_experience(self, amount, title, company, years_experience):
        """Add a salary with experience level"""
        salary_data = {
            "amount": amount,
            "title": title,
            "company": company,
            "experience": years_experience
        }
        self.salaries.append(salary_data)
    
    def calculate_average_salary(self):
        """Calculate average salary"""
        if not self.salaries:
            return 0
        
        total = sum(salary["amount"] for salary in self.salaries)
        return total // len(self.salaries)
    
    def find_salary_range(self):
        """Find minimum, maximum, and range of salaries"""
        if not self.salaries:
            return {"min": 0, "max": 0, "range": 0}
        
        amounts = [salary["amount"] for salary in self.salaries]
        min_salary = min(amounts)
        max_salary = max(amounts)
        
        return {
            "min": min_salary,
            "max": max_salary,
            "range": max_salary - min_salary
        }
    
    def compare_salary_to_market(self, your_salary):
        """Compare your salary to market average"""
        market_average = self.calculate_average_salary()
        
        if market_average == 0:
            return {
                "your_salary": your_salary,
                "market_average": 0,
                "difference": 0,
                "percentage": 0
            }
        
        difference = your_salary - market_average
        percentage = (difference / market_average) * 100
        
        return {
            "your_salary": your_salary,
            "market_average": market_average,
            "difference": difference,
            "percentage": round(percentage, 2)
        }
    
    def calculate_average_by_experience(self, years):
        """Calculate average salary for specific experience level"""
        matching_salaries = [
            salary["amount"] for salary in self.salaries 
            if salary.get("experience") == years
        ]
        
        if not matching_salaries:
            return 0
        
        return sum(matching_salaries) // len(matching_salaries)
    
    def get_companies_above_average(self):
        """Get companies that pay above average"""
        average = self.calculate_average_salary()
        
        above_average_companies = [
            salary["company"] for salary in self.salaries 
            if salary["amount"] > average
        ]
        
        return list(set(above_average_companies))  # Remove duplicates
    
    def calculate_salary_percentile(self, percentile):
        """Calculate salary at specific percentile"""
        if not self.salaries:
            return 0
        
        amounts = sorted([salary["amount"] for salary in self.salaries])
        index = (percentile / 100) * (len(amounts) - 1)
        
        if index.is_integer():
            return amounts[int(index)]
        else:
            # Interpolate between two values
            lower = amounts[int(index)]
            upper = amounts[int(index) + 1]
            return lower + (upper - lower) * (index - int(index))
    
    def get_total_salaries(self):
        """Get total number of salaries"""
        return len(self.salaries)
    
    def clear_salaries(self):
        """Clear all salary data"""
        self.salaries = []
```

## 🎯 **Why This is Perfect for Beginners:**

### **Simple Concepts:**
1. **Basic Math**: Addition, division, percentages
2. **Simple Data Structures**: Lists and dictionaries
3. **Clear Functions**: Each function does one thing
4. **No External Dependencies**: Just Python standard library

### **Real-World Value:**
- Helps with salary negotiations
- Shows market understanding
- Useful for job hunting
- Demonstrates analytical skills

### **TDD Progression:**
- **RED-001**: Basic salary addition and averaging
- **RED-002**: Salary ranges and comparisons
- **RED-003**: Experience-based calculations
- **RED-004**: Percentiles and statistics
- **RED-005**: Data export and analysis

## 🚀 **Usage Example:**

```python
# Super simple usage
calculator = SalaryCalculator()

# Add some market data
calculator.add_salary(70000, "Developer", "Company A")
calculator.add_salary(80000, "Developer", "Company B")
calculator.add_salary(90000, "Developer", "Company C")

# Calculate averages
average = calculator.calculate_average_salary()
print(f"Market average: ${average:,}")

# Compare your salary
comparison = calculator.compare_salary_to_market(75000)
print(f"You're ${comparison['difference']:,} from market average")

# Find best paying companies
best_companies = calculator.get_companies_above_average()
print(f"Companies above average: {best_companies}")
```

This is much more approachable for beginners while still being impressive and useful! Would you like me to show the RED-002 test that would add more sophisticated salary analysis?

```python
import pytest
from salary_calculator import SalaryCalculator

class TestSalaryCalculator:
    """Test the salary calculator for job market analysis"""
    
    def test_create_salary_calculator(self):
        """Test creating a salary calculator"""
        calculator = SalaryCalculator()
        
        assert calculator.salaries == []
        assert calculator.job_title == ""
    
    def test_add_salary(self):
        """Test adding a salary to the calculator"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(75000, "Software Engineer", "Google")
        
        assert len(calculator.salaries) == 1
        assert calculator.salaries[0]["amount"] == 75000
        assert calculator.salaries[0]["title"] == "Software Engineer"
        assert calculator.salaries[0]["company"] == "Google"
    
    def test_calculate_average_salary(self):
        """Test calculating average salary"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(70000, "Developer", "Company A")
        calculator.add_salary(80000, "Developer", "Company B")
        calculator.add_salary(90000, "Developer", "Company C")
        
        average = calculator.calculate_average_salary()
        
        assert average == 80000  # (70000 + 80000 + 90000) / 3
    
    def test_calculate_average_with_no_salaries(self):
        """Test calculating average with no data"""
        calculator = SalaryCalculator()
        
        average = calculator.calculate_average_salary()
        
        assert average == 0
    
    def test_find_salary_range(self):
        """Test finding min and max salaries"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(60000, "Developer", "Company A")
        calculator.add_salary(85000, "Developer", "Company B")
        calculator.add_salary(95000, "Developer", "Company C")
        
        salary_range = calculator.find_salary_range()
        
        assert salary_range["min"] == 60000
        assert salary_range["max"] == 95000
        assert salary_range["range"] == 35000  # 95000 - 60000
    
    def test_compare_salary_to_market(self):
        """Test comparing your salary to market average"""
        calculator = SalaryCalculator()
        
        # Add market data
        calculator.add_salary(70000, "Developer", "Company A")
        calculator.add_salary(80000, "Developer", "Company B")
        calculator.add_salary(90000, "Developer", "Company C")
        
        # Compare your salary
        comparison = calculator.compare_salary_to_market(75000)
        
        assert comparison["your_salary"] == 75000
        assert comparison["market_average"] == 80000
        assert comparison["difference"] == -5000  # 75000 - 80000
        assert comparison["percentage"] == -6.25  # (-5000 / 80000) * 100
    
    def test_calculate_salary_by_experience(self):
        """Test calculating salary based on experience level"""
        calculator = SalaryCalculator()
        
        # Add salaries with experience levels
        calculator.add_salary_with_experience(60000, "Developer", "Company A", 1)
        calculator.add_salary_with_experience(80000, "Developer", "Company B", 3)
        calculator.add_salary_with_experience(100000, "Developer", "Company C", 5)
        
        # Calculate average for 3 years experience
        avg_3_years = calculator.calculate_average_by_experience(3)
        
        assert avg_3_years == 80000
    
    def test_get_companies_above_average(self):
        """Test finding companies that pay above average"""
        calculator = SalaryCalculator()
        
        calculator.add_salary(70000, "Developer", "Company A")
        calculator.add_salary(80000, "Developer", "Company B")
        calculator.add_salary(90000, "Developer", "Company C")
        calculator.add_salary(95000, "Developer", "Company D")
        
        above_average = calculator.get_companies_above_average()
        
        assert len(above_average) == 2  # Company C and D
        assert "Company C" in above_average
        assert "Company D" in above_average
    
    def test_calculate_salary_percentile(self):
        """Test calculating salary percentile"""
        calculator = SalaryCalculator()
        
        # Add 10 salaries
        for i in range(10):
            calculator.add_salary(50000 + (i * 5000), "Developer", f"Company {i}")
        
        # Test 50th percentile (median)
        median = calculator.calculate_salary_percentile(50)
        assert median == 72500  # Middle value
        
        # Test 75th percentile
        percentile_75 = calculator.calculate_salary_percentile(75)
        assert percentile_75 == 87500  # 75% of values are below this
```

```python
class SalaryCalculator:
    """Simple salary calculator for job market analysis"""
    
    def __init__(self):
        self.salaries = []
        self.job_title = ""
    
    def add_salary(self, amount, title, company):
        """Add a salary to the calculator"""
        salary_data = {
            "amount": amount,
            "title": title,
            "company": company
        }
        self.salaries.append(salary_data)
    
    def add_salary_with_experience(self, amount, title, company, years_experience):
        """Add a salary with experience level"""
        salary_data = {
            "amount": amount,
            "title": title,
            "company": company,
            "experience": years_experience
        }
        self.salaries.append(salary_data)
    
    def calculate_average_salary(self):
        """Calculate average salary"""
        if not self.salaries:
            return 0
        
        total = sum(salary["amount"] for salary in self.salaries)
        return total // len(self.salaries)
    
    def find_salary_range(self):
        """Find minimum, maximum, and range of salaries"""
        if not self.salaries:
            return {"min": 0, "max": 0, "range": 0}
        
        amounts = [salary["amount"] for salary in self.salaries]
        min_salary = min(amounts)
        max_salary = max(amounts)
        
        return {
            "min": min_salary,
            "max": max_salary,
            "range": max_salary - min_salary
        }
    
    def compare_salary_to_market(self, your_salary):
        """Compare your salary to market average"""
        market_average = self.calculate_average_salary()
        
        if market_average == 0:
            return {
                "your_salary": your_salary,
                "market_average": 0,
                "difference": 0,
                "percentage": 0
            }
        
        difference = your_salary - market_average
        percentage = (difference / market_average) * 100
        
        return {
            "your_salary": your_salary,
            "market_average": market_average,
            "difference": difference,
            "percentage": round(percentage, 2)
        }
    
    def calculate_average_by_experience(self, years):
        """Calculate average salary for specific experience level"""
        matching_salaries = [
            salary["amount"] for salary in self.salaries 
            if salary.get("experience") == years
        ]
        
        if not matching_salaries:
            return 0
        
        return sum(matching_salaries) // len(matching_salaries)
    
    def get_companies_above_average(self):
        """Get companies that pay above average"""
        average = self.calculate_average_salary()
        
        above_average_companies = [
            salary["company"] for salary in self.salaries 
            if salary["amount"] > average
        ]
        
        return list(set(above_average_companies))  # Remove duplicates
    
    def calculate_salary_percentile(self, percentile):
        """Calculate salary at specific percentile"""
        if not self.salaries:
            return 0
        
        amounts = sorted([salary["amount"] for salary in self.salaries])
        index = (percentile / 100) * (len(amounts) - 1)
        
        if index.is_integer():
            return amounts[int(index)]
        else:
            # Interpolate between two values
            lower = amounts[int(index)]
            upper = amounts[int(index) + 1]
            return lower + (upper - lower) * (index - int(index))
    
    def get_total_salaries(self):
        """Get total number of salaries"""
        return len(self.salaries)
    
    def clear_salaries(self):
        """Clear all salary data"""
        self.salaries = []
```

```python
# Super simple usage
calculator = SalaryCalculator()

# Add some market data
calculator.add_salary(70000, "Developer", "Company A")
calculator.add_salary(80000, "Developer", "Company B")
calculator.add_salary(90000, "Developer", "Company C")

# Calculate averages
average = calculator.calculate_average_salary()
print(f"Market average: ${average:,}")

# Compare your salary
comparison = calculator.compare_salary_to_market(75000)
print(f"You're ${comparison['difference']:,} from market average")

# Find best paying companies
best_companies = calculator.get_companies_above_average()
print(f"Companies above average: {best_companies}")
```

---

**User**

give me the tests, code, and implementation for the skills gap one

---

**Cursor**

Perfect! Here's the **Skills Gap Analyzer** - a simple, math-based tool that's perfect for beginners:

## �� **Skills Gap Analyzer - RED-001**

Here are the tests that will guide the GREEN team:

```python:skills_gap_test.py
import pytest
from skills_gap_analyzer import SkillsGapAnalyzer

class TestSkillsGapAnalyzer:
    """Test the skills gap analyzer for job market analysis"""
    
    def test_create_skills_analyzer(self):
        """Test creating a skills gap analyzer"""
        analyzer = SkillsGapAnalyzer()
        
        assert analyzer.your_skills == []
        assert analyzer.job_requirements == []
        assert analyzer.job_title == ""
    
    def test_add_your_skills(self):
        """Test adding your skills to the analyzer"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        
        assert len(analyzer.your_skills) == 4
        assert "Python" in analyzer.your_skills
        assert "JavaScript" in analyzer.your_skills
        assert "SQL" in analyzer.your_skills
        assert "Git" in analyzer.your_skills
    
    def test_add_job_requirements(self):
        """Test adding job requirements to the analyzer"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        assert len(analyzer.job_requirements) == 4
        assert "Python" in analyzer.job_requirements
        assert "React" in analyzer.job_requirements
        assert "MongoDB" in analyzer.job_requirements
        assert "Docker" in analyzer.job_requirements
    
    def test_calculate_match_percentage(self):
        """Test calculating match percentage between skills and requirements"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        match_percentage = analyzer.calculate_match_percentage()
        
        # Only Python matches out of 4 requirements = 25%
        assert match_percentage == 25.0
    
    def test_calculate_match_percentage_perfect_match(self):
        """Test calculating match percentage with perfect match"""
        analyzer = SkillsGapAnalyzer()
        
        skills = ["Python", "JavaScript", "SQL", "Git"]
        analyzer.add_your_skills(skills)
        analyzer.add_job_requirements(skills)
        
        match_percentage = analyzer.calculate_match_percentage()
        
        # Perfect match = 100%
        assert match_percentage == 100.0
    
    def test_calculate_match_percentage_no_match(self):
        """Test calculating match percentage with no matches"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript"])
        analyzer.add_job_requirements(["Java", "C++"])
        
        match_percentage = analyzer.calculate_match_percentage()
        
        # No matches = 0%
        assert match_percentage == 0.0
    
    def test_find_matching_skills(self):
        """Test finding skills that match job requirements"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        matching_skills = analyzer.find_matching_skills()
        
        assert len(matching_skills) == 1
        assert "Python" in matching_skills
    
    def test_find_missing_skills(self):
        """Test finding skills you don't have but job requires"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        missing_skills = analyzer.find_missing_skills()
        
        assert len(missing_skills) == 3
        assert "React" in missing_skills
        assert "MongoDB" in missing_skills
        assert "Docker" in missing_skills
        assert "Python" not in missing_skills  # You have this
    
    def test_find_extra_skills(self):
        """Test finding skills you have but job doesn't require"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git", "Java"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB"])
        
        extra_skills = analyzer.find_extra_skills()
        
        assert len(extra_skills) == 2
        assert "SQL" in extra_skills
        assert "Git" in extra_skills
        assert "Java" in extra_skills
        assert "Python" not in extra_skills  # Job requires this
    
    def test_prioritize_missing_skills(self):
        """Test prioritizing missing skills by importance"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "Git"])
        analyzer.add_job_requirements_with_importance([
            ("Python", 5),  # High importance
            ("React", 4),   # Medium-high importance
            ("MongoDB", 3), # Medium importance
            ("Docker", 2)   # Low importance
        ])
        
        prioritized = analyzer.prioritize_missing_skills()
        
        # Should be ordered by importance (highest first)
        assert len(prioritized) == 3
        assert prioritized[0] == "React"  # Importance 4
        assert prioritized[1] == "MongoDB"  # Importance 3
        assert prioritized[2] == "Docker"  # Importance 2
    
    def test_calculate_skill_gap_score(self):
        """Test calculating overall skill gap score"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        gap_score = analyzer.calculate_skill_gap_score()
        
        # 2 out of 4 requirements met = 50% score
        assert gap_score == 50.0
    
    def test_get_skills_summary(self):
        """Test getting a complete skills summary"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        summary = analyzer.get_skills_summary()
        
        assert summary["match_percentage"] == 25.0
        assert summary["gap_score"] == 25.0
        assert len(summary["matching_skills"]) == 1
        assert len(summary["missing_skills"]) == 3
        assert len(summary["extra_skills"]) == 2
        assert summary["total_required"] == 4
        assert summary["total_matched"] == 1
    
    def test_clear_skills_data(self):
        """Test clearing all skills data"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript"])
        analyzer.add_job_requirements(["Python", "React"])
        
        analyzer.clear_data()
        
        assert len(analyzer.your_skills) == 0
        assert len(analyzer.job_requirements) == 0
```

And here's the implementation:

```python:skills_gap_analyzer.py
class SkillsGapAnalyzer:
    """Simple skills gap analyzer for job market analysis"""
    
    def __init__(self):
        self.your_skills = []
        self.job_requirements = []
        self.job_title = ""
        self.skill_importance = {}  # For prioritizing skills
    
    def add_your_skills(self, skills):
        """Add your skills to the analyzer"""
        self.your_skills = [skill.lower() for skill in skills]
    
    def add_job_requirements(self, requirements):
        """Add job requirements to the analyzer"""
        self.job_requirements = [req.lower() for req in requirements]
    
    def add_job_requirements_with_importance(self, requirements_with_importance):
        """Add job requirements with importance levels (1-5)"""
        self.job_requirements = [req.lower() for req, _ in requirements_with_importance]
        self.skill_importance = {req.lower(): importance for req, importance in requirements_with_importance}
    
    def calculate_match_percentage(self):
        """Calculate what percentage of job requirements you meet"""
        if not self.job_requirements:
            return 0.0
        
        matching_count = len(self.find_matching_skills())
        return (matching_count / len(self.job_requirements)) * 100
    
    def find_matching_skills(self):
        """Find skills you have that match job requirements"""
        return [skill for skill in self.your_skills if skill in self.job_requirements]
    
    def find_missing_skills(self):
        """Find skills you don't have but job requires"""
        return [req for req in self.job_requirements if req not in self.your_skills]
    
    def find_extra_skills(self):
        """Find skills you have but job doesn't require"""
        return [skill for skill in self.your_skills if skill not in self.job_requirements]
    
    def prioritize_missing_skills(self):
        """Prioritize missing skills by importance level"""
        missing_skills = self.find_missing_skills()
        
        if not self.skill_importance:
            return missing_skills
        
        # Sort by importance (highest first)
        prioritized = sorted(
            missing_skills,
            key=lambda skill: self.skill_importance.get(skill, 1),
            reverse=True
        )
        
        return prioritized
    
    def calculate_skill_gap_score(self):
        """Calculate overall skill gap score (same as match percentage)"""
        return self.calculate_match_percentage()
    
    def get_skills_summary(self):
        """Get a complete summary of skills analysis"""
        matching_skills = self.find_matching_skills()
        missing_skills = self.find_missing_skills()
        extra_skills = self.find_extra_skills()
        
        return {
            "match_percentage": self.calculate_match_percentage(),
            "gap_score": self.calculate_skill_gap_score(),
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
            "extra_skills": extra_skills,
            "total_required": len(self.job_requirements),
            "total_matched": len(matching_skills),
            "total_missing": len(missing_skills),
            "total_extra": len(extra_skills)
        }
    
    def clear_data(self):
        """Clear all skills data"""
        self.your_skills = []
        self.job_requirements = []
        self.skill_importance = {}
    
    def get_total_skills(self):
        """Get total number of your skills"""
        return len(self.your_skills)
    
    def get_total_requirements(self):
        """Get total number of job requirements"""
        return len(self.job_requirements)
    
    def is_skill_match(self, skill):
        """Check if a specific skill matches job requirements"""
        return skill.lower() in self.job_requirements
    
    def get_missing_skills_count(self):
        """Get count of missing skills"""
        return len(self.find_missing_skills())
    
    def get_matching_skills_count(self):
        """Get count of matching skills"""
        return len(self.find_matching_skills())
```

## 🎯 **What This RED-001 Test Reveals:**

The GREEN team will discover they're building:
- A skills comparison system
- Match percentage calculations
- Missing skills identification
- Skills prioritization

**But they won't know yet about:**
- Multiple job comparisons
- Skill development recommendations
- Learning path suggestions
- Market demand analysis

## 🚀 **Usage Examples:**

```python
# Basic usage
analyzer = SkillsGapAnalyzer()

# Add your skills
analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])

# Add job requirements
analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])

# Get analysis
summary = analyzer.get_skills_summary()
print(f"Match percentage: {summary['match_percentage']}%")
print(f"Missing skills: {summary['missing_skills']}")

# With importance levels
analyzer.clear_data()
analyzer.add_your_skills(["Python", "Git"])
analyzer.add_job_requirements_with_importance([
    ("Python", 5),  # Critical
    ("React", 4),   # Important
    ("MongoDB", 3), # Nice to have
    ("Docker", 2)   # Bonus
])

prioritized = analyzer.prioritize_missing_skills()
print(f"Learn these first: {prioritized}")
```

## 🎯 **Why This is Perfect for Beginners:**

### **Simple Concepts:**
1. **List Operations**: Adding, finding, comparing
2. **Basic Math**: Percentages and counting
3. **Simple Logic**: If skill in requirements
4. **Clear Functions**: Each function has one purpose

### **Real-World Value:**
- Helps with job applications
- Guides skill development
- Shows analytical thinking
- Useful for career planning

### **TDD Progression:**
- **RED-001**: Basic skills matching and percentages
- **RED-002**: Multiple job comparisons
- **RED-003**: Skill development recommendations
- **RED-004**: Learning path generation
- **RED-005**: Market demand analysis

This creates a solid foundation that's easy to understand and extend! Would you like me to show the RED-002 test that would add multiple job comparison functionality?

```python
import pytest
from skills_gap_analyzer import SkillsGapAnalyzer

class TestSkillsGapAnalyzer:
    """Test the skills gap analyzer for job market analysis"""
    
    def test_create_skills_analyzer(self):
        """Test creating a skills gap analyzer"""
        analyzer = SkillsGapAnalyzer()
        
        assert analyzer.your_skills == []
        assert analyzer.job_requirements == []
        assert analyzer.job_title == ""
    
    def test_add_your_skills(self):
        """Test adding your skills to the analyzer"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        
        assert len(analyzer.your_skills) == 4
        assert "Python" in analyzer.your_skills
        assert "JavaScript" in analyzer.your_skills
        assert "SQL" in analyzer.your_skills
        assert "Git" in analyzer.your_skills
    
    def test_add_job_requirements(self):
        """Test adding job requirements to the analyzer"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        assert len(analyzer.job_requirements) == 4
        assert "Python" in analyzer.job_requirements
        assert "React" in analyzer.job_requirements
        assert "MongoDB" in analyzer.job_requirements
        assert "Docker" in analyzer.job_requirements
    
    def test_calculate_match_percentage(self):
        """Test calculating match percentage between skills and requirements"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        match_percentage = analyzer.calculate_match_percentage()
        
        # Only Python matches out of 4 requirements = 25%
        assert match_percentage == 25.0
    
    def test_calculate_match_percentage_perfect_match(self):
        """Test calculating match percentage with perfect match"""
        analyzer = SkillsGapAnalyzer()
        
        skills = ["Python", "JavaScript", "SQL", "Git"]
        analyzer.add_your_skills(skills)
        analyzer.add_job_requirements(skills)
        
        match_percentage = analyzer.calculate_match_percentage()
        
        # Perfect match = 100%
        assert match_percentage == 100.0
    
    def test_calculate_match_percentage_no_match(self):
        """Test calculating match percentage with no matches"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript"])
        analyzer.add_job_requirements(["Java", "C++"])
        
        match_percentage = analyzer.calculate_match_percentage()
        
        # No matches = 0%
        assert match_percentage == 0.0
    
    def test_find_matching_skills(self):
        """Test finding skills that match job requirements"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        matching_skills = analyzer.find_matching_skills()
        
        assert len(matching_skills) == 1
        assert "Python" in matching_skills
    
    def test_find_missing_skills(self):
        """Test finding skills you don't have but job requires"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        missing_skills = analyzer.find_missing_skills()
        
        assert len(missing_skills) == 3
        assert "React" in missing_skills
        assert "MongoDB" in missing_skills
        assert "Docker" in missing_skills
        assert "Python" not in missing_skills  # You have this
    
    def test_find_extra_skills(self):
        """Test finding skills you have but job doesn't require"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git", "Java"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB"])
        
        extra_skills = analyzer.find_extra_skills()
        
        assert len(extra_skills) == 2
        assert "SQL" in extra_skills
        assert "Git" in extra_skills
        assert "Java" in extra_skills
        assert "Python" not in extra_skills  # Job requires this
    
    def test_prioritize_missing_skills(self):
        """Test prioritizing missing skills by importance"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "Git"])
        analyzer.add_job_requirements_with_importance([
            ("Python", 5),  # High importance
            ("React", 4),   # Medium-high importance
            ("MongoDB", 3), # Medium importance
            ("Docker", 2)   # Low importance
        ])
        
        prioritized = analyzer.prioritize_missing_skills()
        
        # Should be ordered by importance (highest first)
        assert len(prioritized) == 3
        assert prioritized[0] == "React"  # Importance 4
        assert prioritized[1] == "MongoDB"  # Importance 3
        assert prioritized[2] == "Docker"  # Importance 2
    
    def test_calculate_skill_gap_score(self):
        """Test calculating overall skill gap score"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        gap_score = analyzer.calculate_skill_gap_score()
        
        # 2 out of 4 requirements met = 50% score
        assert gap_score == 50.0
    
    def test_get_skills_summary(self):
        """Test getting a complete skills summary"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript", "SQL"])
        analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])
        
        summary = analyzer.get_skills_summary()
        
        assert summary["match_percentage"] == 25.0
        assert summary["gap_score"] == 25.0
        assert len(summary["matching_skills"]) == 1
        assert len(summary["missing_skills"]) == 3
        assert len(summary["extra_skills"]) == 2
        assert summary["total_required"] == 4
        assert summary["total_matched"] == 1
    
    def test_clear_skills_data(self):
        """Test clearing all skills data"""
        analyzer = SkillsGapAnalyzer()
        
        analyzer.add_your_skills(["Python", "JavaScript"])
        analyzer.add_job_requirements(["Python", "React"])
        
        analyzer.clear_data()
        
        assert len(analyzer.your_skills) == 0
        assert len(analyzer.job_requirements) == 0
```

```python
class SkillsGapAnalyzer:
    """Simple skills gap analyzer for job market analysis"""
    
    def __init__(self):
        self.your_skills = []
        self.job_requirements = []
        self.job_title = ""
        self.skill_importance = {}  # For prioritizing skills
    
    def add_your_skills(self, skills):
        """Add your skills to the analyzer"""
        self.your_skills = [skill.lower() for skill in skills]
    
    def add_job_requirements(self, requirements):
        """Add job requirements to the analyzer"""
        self.job_requirements = [req.lower() for req in requirements]
    
    def add_job_requirements_with_importance(self, requirements_with_importance):
        """Add job requirements with importance levels (1-5)"""
        self.job_requirements = [req.lower() for req, _ in requirements_with_importance]
        self.skill_importance = {req.lower(): importance for req, importance in requirements_with_importance}
    
    def calculate_match_percentage(self):
        """Calculate what percentage of job requirements you meet"""
        if not self.job_requirements:
            return 0.0
        
        matching_count = len(self.find_matching_skills())
        return (matching_count / len(self.job_requirements)) * 100
    
    def find_matching_skills(self):
        """Find skills you have that match job requirements"""
        return [skill for skill in self.your_skills if skill in self.job_requirements]
    
    def find_missing_skills(self):
        """Find skills you don't have but job requires"""
        return [req for req in self.job_requirements if req not in self.your_skills]
    
    def find_extra_skills(self):
        """Find skills you have but job doesn't require"""
        return [skill for skill in self.your_skills if skill not in self.job_requirements]
    
    def prioritize_missing_skills(self):
        """Prioritize missing skills by importance level"""
        missing_skills = self.find_missing_skills()
        
        if not self.skill_importance:
            return missing_skills
        
        # Sort by importance (highest first)
        prioritized = sorted(
            missing_skills,
            key=lambda skill: self.skill_importance.get(skill, 1),
            reverse=True
        )
        
        return prioritized
    
    def calculate_skill_gap_score(self):
        """Calculate overall skill gap score (same as match percentage)"""
        return self.calculate_match_percentage()
    
    def get_skills_summary(self):
        """Get a complete summary of skills analysis"""
        matching_skills = self.find_matching_skills()
        missing_skills = self.find_missing_skills()
        extra_skills = self.find_extra_skills()
        
        return {
            "match_percentage": self.calculate_match_percentage(),
            "gap_score": self.calculate_skill_gap_score(),
            "matching_skills": matching_skills,
            "missing_skills": missing_skills,
            "extra_skills": extra_skills,
            "total_required": len(self.job_requirements),
            "total_matched": len(matching_skills),
            "total_missing": len(missing_skills),
            "total_extra": len(extra_skills)
        }
    
    def clear_data(self):
        """Clear all skills data"""
        self.your_skills = []
        self.job_requirements = []
        self.skill_importance = {}
    
    def get_total_skills(self):
        """Get total number of your skills"""
        return len(self.your_skills)
    
    def get_total_requirements(self):
        """Get total number of job requirements"""
        return len(self.job_requirements)
    
    def is_skill_match(self, skill):
        """Check if a specific skill matches job requirements"""
        return skill.lower() in self.job_requirements
    
    def get_missing_skills_count(self):
        """Get count of missing skills"""
        return len(self.find_missing_skills())
    
    def get_matching_skills_count(self):
        """Get count of matching skills"""
        return len(self.find_matching_skills())
```

```python
# Basic usage
analyzer = SkillsGapAnalyzer()

# Add your skills
analyzer.add_your_skills(["Python", "JavaScript", "SQL", "Git"])

# Add job requirements
analyzer.add_job_requirements(["Python", "React", "MongoDB", "Docker"])

# Get analysis
summary = analyzer.get_skills_summary()
print(f"Match percentage: {summary['match_percentage']}%")
print(f"Missing skills: {summary['missing_skills']}")

# With importance levels
analyzer.clear_data()
analyzer.add_your_skills(["Python", "Git"])
analyzer.add_job_requirements_with_importance([
    ("Python", 5),  # Critical
    ("React", 4),   # Important
    ("MongoDB", 3), # Nice to have
    ("Docker", 2)   # Bonus
])

prioritized = analyzer.prioritize_missing_skills()
print(f"Learn these first: {prioritized}")
```

