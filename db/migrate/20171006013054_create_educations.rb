class CreateEducations < ActiveRecord::Migration[5.1]
  def change
    create_table :educations do |t|
      t.string :school_id
      t.string :school_name
      t.string :school_location
      t.string :linkedin_url
      t.string :school_url

      t.timestamps
    end
  end
end
