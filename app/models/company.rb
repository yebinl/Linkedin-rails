class Company < ApplicationRecord
	has_many :user_in_companies
	has_many :users, :through => :user_in_companies
end
