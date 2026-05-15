from django.urls import path

from .views import (
    ApplicationDetailView,
    ApplicationsView,
    ApplicantsView,
    DashboardIndexView,
    StatisticsView,
    UpdateApplicationStatusView,
    EnrollmentView,
    KanbanBoardView,
    RankingView,
    ExportExcelView,
    EnrollmentOrderView,
    UpdateExamScoreView

)

app_name = 'dashboard'

urlpatterns = [

    path(
        '',
        DashboardIndexView.as_view(),
        name='index'
    ),

    path(
        'applications/',
        ApplicationsView.as_view(),
        name='applications'
    ),

    path(
        'applications/<int:pk>/',
        ApplicationDetailView.as_view(),
        name='application_detail'
    ),

    path(
        'applications/<int:pk>/status/',
        UpdateApplicationStatusView.as_view(),
        name='update_application_status'
    ),

    path(
        'applicants/',
        ApplicantsView.as_view(),
        name='applicants'
    ),

    path(
        'statistics/',
        StatisticsView.as_view(),
        name='statistics'
    ),

    path(
        'ranking/',
        RankingView.as_view(),
        name='ranking'
    ),

    path(
        'enroll/<int:pk>/',
        EnrollmentView.as_view(),
        name='enrollment'
    ),

    path(
        'kanban/',
        KanbanBoardView.as_view(),
        name='kanban'
    ),
    path(
        'export/excel/',
        ExportExcelView.as_view(),
        name='export_excel'
    ),
    path(
        'enrollment-order/',
        EnrollmentOrderView.as_view(),
        name='enrollment_order'
    ),
    path(
    'applications/<int:pk>/score/',
    UpdateExamScoreView.as_view(),
    name='update_score'
),

]