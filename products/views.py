from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import *
from .forms import AddReviewForm, UpdateReviewForm, ShoesForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.


class CategoryProductsListView(View):
    def get(self, request):
        categories = CategoryProducts.objects.all()
        return render(request, 'category_products.html', {'categories': categories})


class ShoesListView(View):
    def get(self, request):
        category = get_object_or_404(CategoryProducts, pk=category_id)
        shoes = Shoes.objects.filter(category=category)
        return render(request, 'products/shoes.html', {'shoes': shoes})


class ShoesListView1(ListView):
    model = Shoes
    template_name = 'products/shoes_list.html'
    context_object_name = 'shoes'


class ShoesDetailView(View):
    def get(self, request, pk):
        shoe = get_object_or_404(Shoes, pk=pk)
        reviews = Review.objects.filter(shoe=shoe)
        return render(request, 'products/shoe_detail.html', {'shoe': shoe, 'reviews': reviews})


class CreateShoeView(View):
    def get(self, request):
        form = ShoesForm()
        return render(request, 'createshoe.html', {'form': form})

    def post(self, request):
        form = ShoesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products:all_shoes')
        return render(request, 'createshoe.html', {'form': form})


class ShoesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Shoes
    form_class = ShoesForm
    template_name = 'products/shoes_form.html'

    def test_func(self):
        shoe = self.get_object()
        return self.request.user == shoe.owner or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to update this shoe.")
        return redirect('shoes_detail', pk=self.get_object().pk)

    def get_success_url(self):
        messages.success(self.request, "Shoe updated successfully!")
        return reverse('shoes_detail', kwargs={'pk': self.object.pk})


class ShoesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Shoes
    template_name = 'products/shoes_confirm_delete.html'
    success_url = reverse_lazy('shoes_list')

    def test_func(self):
        shoe = self.get_object()
        return self.request.user == shoe.owner or self.request.user.is_staff

    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to delete this shoe.")
        return redirect('shoes_detail', pk=self.get_object().pk)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Shoe deleted successfully!")
        return super().delete(request, *args, **kwargs)


class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        shoe = get_object_or_404(Shoes, pk=pk)
        add_review_form = AddReviewForm()
        return render(request, 'products/add_review.html', {'shoe': shoe, 'add_review_form': add_review_form})

    def post(self, request, pk):
        shoe = get_object_or_404(Shoes, pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = add_review_form.save(commit=False)
            review.shoe = shoe
            review.user = request.user
            review.save()
            messages.success(request, "Your review was added successfully!")
            return redirect('products:shoe_detail', pk=pk)
        else:
            messages.error(request, "Failed to add your review.")
            return render(request, 'products/add_review.html', {'shoe': shoe, 'add_review_form': add_review_form})


class ReviewDeleteView(View):
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        shoe_pk = review.shoe.pk
        if review.user == request.user or request.user.is_staff:
            review.delete()
            messages.success(request, "Your review was deleted successfully!")
        else:
            messages.error(request, "You do not have permission to delete this review.")
        return redirect('products:shoe_detail', pk=shoe_pk)


class ReviewUpdateView(View):
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if review.user != request.user and not request.user.is_staff:
            messages.error(request, "You do not have permission to update this review.")
            return redirect('products:shoe_detail', pk=review.shoe.pk)
        update_form = UpdateReviewForm(instance=review)
        return render(request, 'products/update_review.html', {'form': update_form})

    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        if review.user != request.user and not request.user.is_staff:
            messages.error(request, "You do not have permission to update this review.")
            return redirect('products:shoe_detail', pk=review.shoe.pk)
        update_form = UpdateReviewForm(request.POST, instance=review)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, "Your review was updated successfully!")
            return redirect('products:shoe_detail', pk=review.shoe.pk)
        else:
            messages.error(request, "Failed to update your review.")
            return render(request, 'products/update_review.html', {'form': update_form})


class SearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        shoes_results = Shoes.objects.filter(name__icontains=query)
        return render(request, 'products/search_results.html', {
            'query': query,
            'shoes_results': shoes_results,
        })
