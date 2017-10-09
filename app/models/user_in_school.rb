class UserInSchool < ApplicationRecord
	belongs_to :user
	belongs_to :education
end
