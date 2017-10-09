class User < ApplicationRecord
	has_many :user_in_companies
	has_many :companies, :through => :user_in_companies
	has_many :user_in_schools
	has_many :educations, :through => :user_in_schools
end
