class Education < ApplicationRecord
	has_many :user_in_schools
	has_many :users, :through => :user_in_schools
end
