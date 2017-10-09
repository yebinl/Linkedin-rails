json.extract! user_in_company, :id, :user_id, :company_id, :start_date, :end_date, :position, :description, :created_at, :updated_at
json.url user_in_company_url(user_in_company, format: :json)
