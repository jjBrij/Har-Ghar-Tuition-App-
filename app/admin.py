from django.contrib import admin
from .models import Teacher, TutorApplication, Student, SubjectResult

# Register the Teacher model with a custom admin interface
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_10_percentage', 'class_12_percentage', 'degree_name', 'degree_percentage')
    search_fields = ('name',)

admin.site.register(Teacher, TeacherAdmin)

# Register the TutorApplication model with a custom admin interface
@admin.register(TutorApplication)
class TutorApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'class_of_study', 'num_children', 'contact_number')
    search_fields = ('name', 'email', 'class_of_study')

# Inline form to manage subjects for each student
class SubjectInline(admin.TabularInline):
    model = SubjectResult
    extra = 1  # Initially show only 1 subject entry form

# Register the StudentResult model with a custom admin interface
class StudentResultAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'roll_no')
    search_fields = ('roll_no', 'student_name')
    inlines = [SubjectInline]  # Allows subjects to be managed inline

admin.site.register(Student, StudentResultAdmin)

from .models import SubjectResult

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'full_marks', 'passing_marks', 'obtained_marks', 'student_result')
    search_fields = ('subject_name', 'student_result__student_name')  # Allows searching by subject name or student name
    list_filter = ('student_result',)  # Filters by the associated StudentResult
    ordering = ('student_result',)  # Ordering by student result (ascending by default)

admin.site.register(SubjectResult, SubjectAdmin)


from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'amount', 'transaction_id', 'created_at']
    search_fields = ['name', 'student_id', 'transaction_id']
