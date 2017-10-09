class CreateUserInSchools < ActiveRecord::Migration[5.1]
  def change
    create_table :user_in_schools do |t|
      t.string :user_id
      t.string :school_id
      t.string :start_date
      t.string :end_date
      t.string :degree
      t.string :description
      t.string :fields
      t.string :linkedin_id
      t.string :string

      t.timestamps
    end
  end
end
