json.extract! company, :id, :company_id, :company_name, :company_location, :linkedin_url, :company_url, :industry, :created_at, :updated_at
json.url company_url(company, format: :json)
