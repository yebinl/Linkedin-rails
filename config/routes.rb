Rails.application.routes.draw do
  resources :user_in_schools
  resources :user_in_companies
  resources :educations
  resources :companies
  resources :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'users#index'
end
