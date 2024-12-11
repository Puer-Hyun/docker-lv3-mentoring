-- 언어 테이블
CREATE TABLE supported_languages (
    language_id INT AUTO_INCREMENT PRIMARY KEY,
    language_code VARCHAR(10) NOT NULL UNIQUE,
    language_name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 웹 페이지 콘텐츠 테이블
CREATE TABLE page_contents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(2048) NOT NULL,
    language_id INT NOT NULL,
    full_content MEDIUMTEXT NOT NULL,
    summarization TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (language_id) REFERENCES supported_languages(language_id)
);

-- 기본 언어 데이터 삽입
INSERT INTO supported_languages (language_code, language_name) VALUES 
    ('ko', '한국어'),
    ('en', 'English');    -- 세미콜론 추가