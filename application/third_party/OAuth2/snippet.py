	RewriteCond %{SERVER_PORT} !443
	RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L]