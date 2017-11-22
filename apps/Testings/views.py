from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DeleteView, CreateView, UpdateView, DetailView

from apps.Testings.models import Keyword, Collection, TestCase, TestSuite
from apps.Testings.forms import CollectionForm, ImportScriptForm, EditImportScriptForm


class KeyWordsView(LoginRequiredMixin, TemplateView):
    template_name = "keywords.html"


class NewKeywordView(LoginRequiredMixin, TemplateView):
    template_name = "create-keyword.html"


class EditKeywordView(LoginRequiredMixin, DetailView):
    model = Keyword
    template_name = "edit-keyword.html"


class DeleteKeywordView(LoginRequiredMixin, DeleteView):
    template_name = "delete-keyword.html"
    model = Keyword
    success_url = reverse_lazy('keywords')


class TestcaseView(LoginRequiredMixin, TemplateView):
    template_name = "testcases.html"


class NewTestcaseView(LoginRequiredMixin, TemplateView):
    template_name = "create-testcase.html"


class EditTestcaseView(LoginRequiredMixin, DetailView):
    model = TestCase
    template_name = "edit-testcase.html"


class DeleteTestcaseView(LoginRequiredMixin, DeleteView):
    template_name = "delete-testcase.html"
    model = TestCase
    success_url = reverse_lazy('testcases')


class TestsuiteView(LoginRequiredMixin, TemplateView):
    template_name = "testsuites.html"


class NewTestsuiteView(LoginRequiredMixin, TemplateView):
    template_name = "create-testsuites.html"


class EditTestsuiteView(LoginRequiredMixin, DetailView):
    model = TestSuite
    template_name = "edit-testsuites.html"


class DeleteTestsuiteView(LoginRequiredMixin, DeleteView):
    template_name = "delete-testsuite.html"
    model = TestSuite

    def get_success_url(self):
        messages.success(self.request, "Test Suite Deleted")
        return reverse_lazy("testsuites")


class CollectionsView(LoginRequiredMixin, TemplateView):
    template_name = "collections.html"


class NewCollectionsView(LoginRequiredMixin, CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = "create-edit-collection.html"

    def get_success_url(self):
        messages.success(self.request, "Collection Created")
        return reverse_lazy('collections')

    def get_context_data(self, **kwargs):
        context = super(NewCollectionsView, self).get_context_data(**kwargs)
        context['title'] = "New Collection"
        return context


class EditCollectionsView(LoginRequiredMixin, UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = "create-edit-collection.html"

    def get_success_url(self):
        messages.success(self.request, "Collection Edited")
        return reverse_lazy('collections')

    def get_context_data(self, **kwargs):
        context = super(EditCollectionsView, self).get_context_data(**kwargs)
        context['title'] = "Edit Collections"
        return context


class DeleteCollectionsView(LoginRequiredMixin, DeleteView):
    model = Collection
    template_name = "delete-collections.html"

    def get_success_url(self):
        messages.success(self.request, "Colletions Deleted")
        return reverse_lazy('collections')


class NewKeywordImportedView(LoginRequiredMixin, CreateView):
    template_name = "import-script.html"
    form_class = ImportScriptForm
    model = Keyword

    def form_valid(self, form):
        file = form.files.get('file_script')
        if file:
            form.instance.script = file.read()
            form.instance.user = self.request.user
            form.instance.script_type = 2
            form.save()
        messages.success(self.request, "Script imported")
        return super(NewKeywordImportedView, self).form_valid(form)

    def form_invalid(self, form):
        return super(NewKeywordImportedView, self).form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('keywords')


class EditKeywordImportedView(LoginRequiredMixin, UpdateView):
    form_class = EditImportScriptForm
    template_name = "edit-import-script.html"
    model = Keyword
